
from exceptions import InvalidResponse


class Staff:
    """AniList Staff Object"""
    def __init__(self, staff, session, token, small=False):
        self.session = session
        self.token = token

        self.id = staff['id']
        self.name_first = staff['name_first']
        self.name_last = staff['name_last']
        self.image_url_lge = staff['image_url_lge']
        self.image_url_med = staff['image_url_med']
        self.language = staff['language']
        self.role = staff['role']

        if not small:
            self.dob = staff['dob']
            self.website = staff['website']
            self.info = staff['info']
            self.name_first_japanese = staff['name_first_japanese']
            self.name_last_japanese = staff['name_last_japanese']
            self.name_jp = self.name_last_japanese + self.name_first_japanese

    async def get_page(self):
        pass
