
# Having ujson will give you a free performance boost.
try:
    import ujson as json
except ImportError:
    import json

from exceptions import InvalidResponse


class User:
    """AniList User Object"""
    def __init__(self, user, session, token, small=False):
        """Returns a User Object.

        Parameters:
        -----------
        user : dict
            User object Response from AniList
        small=False : bool
            True if user object is small.
        """
        self.session = session
        self.url = 'https://anilist.co/api/'
        self.token = token
        self.id = user['id']
        self.display_name = user['display_name']
        self.image_url_lge = user.get('image_url_lge', None)
        self.image_url_med = user.get('image_url_med', None)

        if not small:
            self.anime_time = user.get('anime_time', 0)
            self.manga_chap = user.get('manga_chap', 0)
            self.about = user.get('about', 'This user has no About section.')
            self.list_order = user.get('list_order', 0)
            self.adult_content = user.get('adult_content', False)
            self.following = user.get('following', False)
            self.image_url_banner = user.get('image_url_banner', None)
            self.title_language = user.get('title_language', None)
            self.score_type = user.get('score_type', None)
            self.custom_list_anime = user.get('list_order', [])
            self.custom_list_manga = user.get('list_order', [])
            self.advanced_rating = user.get('advanced_rating', False)
            self.advanced_rating_names = user.get('advanced_rating_names', [])
            self.notifications = user.get('notifications', 0)

    async def get_activity(self, page: int=0):
        async with self.session.get(
            self.url + 'user/' + str(self.id) + '/activity?page=' +
            str(page) + '&access_token=' + self.token.access_token
        ) as resp:
            if resp.status != 200:
                print('ERROR: AniListUser returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "user.get_activity did not receive status 200.")
            return await resp.json(loads=json.loads)

    async def get_following(self):
        async with self.session.get(
            self.url + 'user/' + str(self.id) + '/following?access_token=' + self.token.access_token
        ) as resp:
            if resp.status != 200:
                print('ERROR: AniListUser returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "user.get_activity did not receive status 200.")
            return await resp.json(loads=json.loads)

    async def get_follwers(self):
        async with self.session.get(
            self.url + 'user/' + str(self.id) + '/followers?access_token=' + self.token.access_token
        ) as resp:
            if resp.status != 200:
                print('ERROR: AniListUser returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "user.get_activity did not receive status 200.")
            return await resp.json(loads=json.loads)

    async def get_favourites(self):
        async with self.session.get(
            self.url + 'user/' + str(self.id) + '/favourites?access_token=' + self.token.access_token
        ) as resp:
            if resp.status != 200:
                print('ERROR: AniListUser returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "user.get_activity did not receive status 200.")
            return await resp.json(loads=json.loads)

    async def get_anime_list(self, raw=False):
        async with self.session.get(
            self.url + 'user/' + str(self.id) + '/animelist' +
            ('/raw' if raw else '') + '?access_token=' + self.token.access_token
        ) as resp:
            if resp.status != 200:
                print('ERROR: AniListUser returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "user.get_activity did not receive status 200.")
            return await resp.json(loads=json.loads)

    async def get_manga_list(self, raw=False):
        async with self.session.get(
            self.url + 'user/' + str(self.id) + '/mangalist' +
            ('/raw' if raw else '') + '?access_token=' + self.token.access_token
        ) as resp:
            if resp.status != 200:
                print('ERROR: AniListUser returned error code : ' + str(resp.status))
                raise AuthenticationError(resp.status, "user.get_activity did not receive status 200.")
            return await resp.json(loads=json.loads)
