class ProducerNotFoundException(Exception):
    def __init__(self, message="Producer not found.", code=400):
        self.message = message
        self.code = code


class ProductCategoryNotFoundException(Exception):
    def __init__(self, message="Product category not found.", code=400):
        self.message = message
        self.code = code


class ProductNotFoundException(Exception):
    def __init__(self, message="Product not found", code=400):
        self.message = message
        self.code = code


class ProductQuantityInStockSubtractionError(Exception):
    def __init__(self, message="Quantity in stock can not be under 0.", code=400):
        self.message = message
        self.code = code
