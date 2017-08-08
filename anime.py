

try:
    import ujson as json
except ImportError:
    import json

from exceptions import InvalidResponse


class Anime:
    """AniList Anime Object"""
    def __init__(self, anime, session, token, small=False):
        """Returns an Anime Object.
        These objects will not support deprecated values.
        Start/End Date are referring to Fuzzy objects, just shortened for brevity.

        Parameters:
        -----------
        anime : dict
            Anime object Response from AniList
        session: aiohttp.session()
            A aiohttp Session.
        small=False : bool
            True if user object is small.
        """
        self.session = session
        self.url = 'https://anilist.co/api/'
        self.token = token
        self.id = anime['id']
        self.series_type = anime['series_type']
        self.title_romaji = anime['title_romaji']
        self.title_english = anime['title_english']
        self.title_japanese = anime['title_japanese']
        self.type = anime['type']
        self.start_date = anime['start_date_fuzzy']
        self.end_date = anime['end_date_fuzzy']
        self.synonyms = anime['synonyms']
        self.genres = anime['genres']
