

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
        self.adult = anime['adult']
        self.average_score = anime['average_score']
        self.popularity = anime['popularity']
        self.img_url_sml = anime['img_url_sml']
        self.img_url_med = anime['img_url_med']
        self.img_url_lge = anime['image_url_lge']
        self.updated_at = anime['updated_at']
        self.total_episodes = anime['total_episodes']
        self.airing_status = anime.get('airing_status', None)
        if not small:
            self.season = anime.get('season', None)
            self.description = anime.get('description', None)
            self.favourite = anime.get('favourite', None)
            self.img_url_banner = anime.get('img_url_banner', None)
            self.score_distribution = anime.get('score_distribution', [])
            self.list_stats = anime.get('list_stats', [])
            self.duration = anime.get('duration', None)
            self.youtube_id = anime.get('youtube_id', None)
            self.hashtag = anime.get('hashtag', None)
            self.source = anime.get('source', None)


