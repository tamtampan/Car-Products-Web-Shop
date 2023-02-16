
class ShoppingCartNotFoundException(Exception):
    def __init__(self, message="Shopping cart not found.", code=400):
        self.message = message
        self.code = code


class ShoppingCartTotalCostError(Exception):
    def __init__(self, message="Total cost can not be under 0.", code=400):
        self.message = message
        self.code = code


class CartItemNotFoundException(Exception):
    def __init__(self, message="Cart item not found", code=400):
        self.message = message
        self.code = code
