""" This is an asynchronous API wrapper for AniList """

import asyncio
import time

import aiohttp

# Having ujson will give you a free performance boost.
try:
    import ujson as json
except ImportError:
    import json

from anime import Anime
from character import Character
from exceptions import InvalidResponse
from manga import Manga
from staff import Staff
from studio import Studio
from user import User


class AniListClient:
    """ An AniList Client """

    def __init__(self, client_id, client_secret, client_pin, loop=None):
        """Returns an AniListClient Instance

        Parameters
        ----------
        client_id : str
            AniList Client ID
        client_secret: str
            AniList Client Secret
        client_pin: str
            Anilist Client PIN.
            If you don't have one, please use the following link:
            https://anilist.co/api/auth/authorize?grant_type=authorization_pin&client_id=YOUR_CLIENT_ID&response_type=pin'
            Client_Pin will not be held in the memory once a connection is established.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        if loop:
            self.loop = loop
        else:
            self.loop = asyncio.get_event_loop()
        self.url = 'https://anilist.co/api/'
        self.session = aiohttp.ClientSession(loop=self.loop, json_serialize=json.dumps)
        self.time = 0
        self.access_token, self.refresh_token = None, None
        self.loop.run_until_complete(self._get_access_token(client_pin))

    async def _get_access_token(self, client_pin):
        async with self.session.post(
            self.url + 'auth/access_token',
            data={
                'grant_type': 'authorization_pin',
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'code': client_pin
            }
        ) as resp:
            if resp.status != 200:
                print('ERROR: AniListSession returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "Did not receive status 200.")
            response = await resp.json(loads=json.loads)
        self.access_token = response['access_token']
        self.refresh_token = response['refresh_token']

    async def _refresh_access_token(self):
        t = time.time()
        if t - self.time >= 3600:
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

    async def get_user(self, user: str):
        await self._refresh_access_token()
        async with self.session.get(
            self.url + 'user/' + user
        ) as resp:
            if resp.status != 200:
                print('ERROR: AniListClient returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "Did not receive status 200.")
            response = await resp.json(loads=json.loads)
            return User(response, self.session)

    async def search_users(self, query: str):
        pass

    async def get_activity(self):
        pass

    async def get_following(self):
        pass

    async def get_follwers(self):
        pass

    async def get_favorites(self):
        pass

    async def get_anime_list(self):
        pass

    async def get_manga_list(self):
        pass

    async def create_activity(self):
        pass

    async def delete_activity(self):
        pass

    async def get_notifications(self):
        pass

    async def follow(self):
        pass

    async def unfollow(self):
        pass

    async def get_user_airing(self):
        pass

    async def create_anime_list_entry(self):
        pass

    async def edit_anime_list_entry(self):
        pass

    async def remove_anime_list_entry(self):
        pass

    async def create_manga_list_entry(self):
        pass

    async def edit_manga_list_entry(self):
        pass

    async def remove_manga_list_entry(self):
        pass
