
class OfficeNotFoundException(Exception):
    def __init__(self, message="Office not found.", code=400):
        self.message = message
        self.code = code
