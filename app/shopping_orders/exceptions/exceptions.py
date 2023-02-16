
class ShoppingOrderNotFoundException(Exception):
    def __init__(self, message="Shopping order not found.", code=400):
        self.message = message
        self.code = code
