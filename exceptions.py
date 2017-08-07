
class InvalidResponse(Exception):
    """ Error for Bad Authentication """
    def __init__(self, status, reason):
        self.status = status
        self.reason = reason