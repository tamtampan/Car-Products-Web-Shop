
class ShoppingCartNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ShoppingCartTotalCostError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class CartItemNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
