"""Producer Exceptions"""


class ProducerNotFoundError(Exception):
    """Not Found Error"""

    def __init__(self, message="Producer not found.", code=400):
        self.message = message
        self.code = code


class ProductCategoryNotFoundError(Exception):
    """Product category not found"""

    def __init__(self, message="Product category not found.", code=400):
        self.message = message
        self.code = code


class ProductNotFoundError(Exception):
    """Product not found"""

    def __init__(self, message="Product not found", code=400):
        self.message = message
        self.code = code


class ProductQuantityInStockSubtractionError(Exception):
    """Error when quantity stock under 0"""

    def __init__(self, message="Quantity in stock can not be under 0.", code=400):
        self.message = message
        self.code = code


class ProductCodeNotFoundError(Exception):
    """Product code not found"""

    def __init__(self, message="Product with provided code not found.", code=400):
        self.message = message
        self.code = code


class ProductOutOfStockError(Exception):
    """Product out of stock"""

    def __init__(self, message="Product is currently out of stock.", code=400):
        self.message = message
        self.code = code
