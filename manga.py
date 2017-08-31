
from exceptions import InvalidResponse


class Manga:
    """AniList Manga Object"""
    def __init__(self, manga, session, token, small=False):
        """Returns a Manga Object.
        These objects will not support deprecated values.
        Start/End Date are referring to Fuzzy objects, just shortened for brevity.

        Parameters:
        -----------
        manga : dict
            Anime object Response from AniList
        session: aiohttp.session()
            A aiohttp Session.
        small=False : bool
            True if user object is small.
        """
        self.session = session
        self.url = 'https://anilist.co/api/'
        self.token = token
        self.id = manga['id']
        self.series_type = manga['series_type']
        self.title_romaji = manga['title_romaji']
        self.title_english = manga['title_english']
        self.title_japanese = manga['title_japanese']
        self.type = manga['type']
        self.start_date = manga['start_date_fuzzy']
        self.end_date = manga['end_date_fuzzy']
        self.synonyms = manga['synonyms']
        self.genres = manga['genres']
        self.adult = manga['adult']
        self.average_score = manga['average_score']
        self.popularity = manga['popularity']
        self.img_url_sml = manga['img_url_sml']
        self.img_url_med = manga['img_url_med']
        self.img_url_lge = manga['image_url_lge']
        self.updated_at = manga['updated_at']
        self.total_chapters = manga['total_chapters']
        self.publishing_status = manga.get('publishing_status', None)
        if not small:
            self.season = manga.get('season', None)
            self.description = manga.get('description', None)
            self.favourite = manga.get('favourite', None)
            self.img_url_banner = manga.get('img_url_banner', None)
            self.score_distribution = manga.get('score_distribution', [])
            self.list_stats = manga.get('list_stats', [])
            self.total_volumes = manga['total_volumes']