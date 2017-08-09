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
        self.user = None
        self.loop.run_until_complete(self.get_current_user())

    async def get_current_user(self):
        async with self.session.get(
            self.url + 'user?access_token=' + self.token.access_token
        ) as resp:
            if resp.status != 200:
                print('ERROR: AniListClient returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "Did not receive status 200.")
            response = await resp.json(loads=json.loads)
            self.user = User(response, self.session)

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
        """ Returns Array of User Objects."""
        async with self.session.get(
            self.url + 'user/search/' + query + '?access_token=' + self.token.access_token
        ) as resp:
            if resp.status != 200
                print('ERROR: AniListClient returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "Did not receive status 200.")
            response = await resp.json(loads=json.loads)
            if response.get('error', False):
                return None
            users = []
            for x in response:
                users.append(User(x, self.session))

            return users

    async def get_activity(self, page: int=0):
        """ Return current user's activity feed."""
        await self.user.get_activity(page)

    async def get_following(self):
        await self.user.get_following()

    async def get_followers(self):
        await self.user.get_followers()

    async def get_favourites(self):
        await self.user.get_favourites()

    async def get_anime_list(self, raw=False):
        await self.user.get_anime_list(raw)

    async def get_manga_list(self, raw=False):
        await self.user.get_manga_list(raw)

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

    async def get_character(self, id):
        pass

    async def favourite_character(self, id):
        pass

    async def search_character(self, query):
        pass

    async def get_staff(self, id):
        pass

    async def get_actor(self, id):
        pass

    async def favourite_staff(self, id):
        pass

    async def favourite_actor(self, id):
        pass

    async def search_staff(self, query):
        pass

    async def search_actor(self, query):
        pass

    async def get_studio(self, id):

    async def search_studio(self, query):
        pass

