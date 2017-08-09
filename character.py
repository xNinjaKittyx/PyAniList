
from exceptions import InvalidResponse


class Character:
    """AniList Character Object"""
    def __init__(self, character, session, token, small=False):
        self.session = session
        self.token = token
        self.id = character['id']
        self.name_first = character['name_first']
        self.name_last = character['name_last']
        self.image_url_lge = character['image_url_lge']
        self.image_url_med = character['image_url_med']
        self.role = character['role']

        if not small:
            self.name_alt = character.get('name_alt', None)
            self.info = character.get('info', None)
            self.name_japanese = character.get('name_japanese', None)

    async def get_page(self):
        pass