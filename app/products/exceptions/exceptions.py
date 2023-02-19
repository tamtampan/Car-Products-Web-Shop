class ProducerNotFoundError(Exception):
    def __init__(self, message="Producer not found.", code=400):
        self.message = message
        self.code = code


class ProductCategoryNotFoundError(Exception):
    def __init__(self, message="Product category not found.", code=400):
        self.message = message
        self.code = code


class ProductNotFoundError(Exception):
    def __init__(self, message="Product not found", code=400):
        self.message = message
        self.code = code


class ProductQuantityInStockSubtractionError(Exception):
    def __init__(self, message="Quantity in stock can not be under 0.", code=400):
        self.message = message
        self.code = code


class ProductCodeNotFoundError(Exception):
    def __init__(self, message="Product with provided code not found.", code=400):
        self.message = message
        self.code = code


class ProductOutOfStockError(Exception):
    def __init__(self, message="Product is currently out of stock.", code=400):
        self.message = message
        self.code = code
