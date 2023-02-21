class ShoppingOrderNotFoundError(Exception):
    def __init__(self, message="Shopping order not found.", code=400):
        self.message = message
        self.code = code


class ShoppingOrderItemNotFoundError(Exception):
    def __init__(self, message="Shopping order item not found.", code=400):
        self.message = message
        self.code = code


class ShoppingOrderTotalPriceSubtractionError(Exception):
    def __init__(self, message="Shopping order total price can not be under 0.", code=400):
        self.message = message
        self.code = code


class DateNotValid(Exception):
    def __init__(self, message="Date not valid. Date should be after 2020-01-01 and before 2030-01-01.", code=400):
        self.message = message
        self.code = code
