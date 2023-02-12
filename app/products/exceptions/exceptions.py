class ProducerNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ProductCategoryNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ProductNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ProductQuantityInStockError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
