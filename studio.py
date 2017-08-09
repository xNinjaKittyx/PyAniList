
from exceptions import InvalidResponse


class Studio:
    """AniList Studio Object"""
    def __init__(self, studio, session, token):
        self.session = session
        self.token = token

        self.studio_name = studio['studio_name']
        self.studio_wiki = studio['studio_wiki']
        self.id = studio['id']
        self.main_studio = studio['main_studio']

    async def get_page(self):
