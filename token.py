

class Token:

    def __init__(self, loop, session, client_id, client_secret, client_pin):
        self.loop = loop
        self.session = session
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_pin = client_pin
        self.access_token, self.refresh_token = self.loop.run_until_complete(self._get_access_token())
        self.loop.create_task(self._refresh_access_token())

    async def _get_access_token(self):
        async with self.session.post(
            self.url + 'auth/access_token',
            data={
                'grant_type': 'authorization_pin',
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'code': self.client_pin
            }
        ) as resp:
            if resp.status != 200:
                print('ERROR: AniListSession returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "Did not receive status 200.")
            response = await resp.json(loads=json.loads)
            return response['access_token'], response['refresh_token']

    async def _refresh_access_token(self):
        while True:
            t = asyncio.time()
            if t - self.time >= 3590:
                self.time = t
                async with self.session.post(
                    self.url + 'auth/access_token',
                    data={
                        'grant_type': 'refresh_token',
                        'client_id': self.client_id,
                        'client_secret': self.client_secret,
                        'code': self.refresh_token
                    }
                ) as resp:
                    if resp.status != 200:
                        print('ERROR: AniListSession returned error code : ' + str(resp.status))
                        raise AuthenticationError(resp.status, "Did not receive status 200.")
                    response = await resp.json(loads=json.loads)
                    self.access_token = response['access_token']
            asyncio.sleep(1)