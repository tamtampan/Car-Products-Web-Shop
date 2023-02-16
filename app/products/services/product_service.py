from app.products.repositories.product_repository import ProductRepository
from app.db.database import SessionLocal


class ProductService:

    @staticmethod
    def create(name: str, description: str, code: str, price: float, for_car_brand: str,
               quantity_in_stock: int, producer_id: str, product_category_id: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.create(name, description, code, price, for_car_brand, quantity_in_stock,
                                                 producer_id, product_category_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(product_id: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.read_by_id(product_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.read_all()
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(product_id: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.delete_by_id(product_id)
        except Exception as e:
            raise e

    @staticmethod
    def update(product_id: str, name: str = None, description: str = None, price: float = None,
               for_car_brand: str = None, quantity_in_stock: int = None):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.update(product_id, name, description, price, for_car_brand, quantity_in_stock)
        except Exception as e:
            raise e

    @staticmethod
    def update_quantity_in_stock(product_id: str, amount: int, subtract: bool = False):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.update_quantity_in_stock(product_id, amount, subtract)
        except Exception as e:
            raise e

    @staticmethod
    def read_products_for_car_brand(car_brand: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.read_products_for_car_brand(car_brand)
        except Exception as e:
            raise e

    @staticmethod
    def read_products_by_category_id(product_category_id: str):
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.read_products_by_category_id(product_category_id)
        except Exception as e:
            raise e
