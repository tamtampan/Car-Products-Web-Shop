
class ShoppingCartNotFoundError(Exception):
    """This class is used to raise an exception when a shopping cart is not found"""
    def __init__(self, message="Shopping cart not found.", code=400):
        self.message = message
        self.code = code


class ShoppingCartTotalCostError(Exception):
    def __init__(self, message="Total cost can not be below 0.", code=400):
        self.message = message
        self.code = code


class CartItemNotFoundError(Exception):
    def __init__(self, message="Cart item not found.", code=400):
        self.message = message
        self.code = code


class QuantityNotValid(Exception):
    def __init__(self, message="Quantity can not be below 1 or over 20.", code=400):
        self.message = message
        self.code = code
