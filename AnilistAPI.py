""" This is an asynchronous API wrapper for AniList """

import asyncio

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
from token import Token
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
        self.token = Token(self.loop, self.session, self.client_id, self.client_secret, self.refresh_token)

    async def get_user(self, user: str):
        async with self.session.get(
            self.url + 'user/' + user + '?access_token=' + self.token.access_token
        ) as resp:
            if resp.status != 200:
                print('ERROR: AniListClient returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "Did not receive status 200.")
            response = await resp.json(loads=json.loads)
            return User(response, self.session)

    async def search_users(self, query: str):
        async with self.session.get(
            self.url + 'user/search/' + query + '?access_token=' + self.token.access_token
        )
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
