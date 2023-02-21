from app.products.repositories.product_repository import ProductRepository
from app.db.database import SessionLocal
from app.products.exceptions import *
import operator
from sqlalchemy.exc import IntegrityError


class ProductService:

    @staticmethod
    def create(name: str, description: str, code: str, price: float, for_car_brand: str,
               quantity_in_stock: int, producer_id: str, product_category_id: str) -> object:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                return product_repository.create(name, description, code, price, for_car_brand, quantity_in_stock,
                                                 producer_id, product_category_id)
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(product_id: str) -> object:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                product = product_repository.read_by_id(product_id)
                if product is None:
                    raise ProductNotFoundError()
                return product
        except Exception as e:
            raise e

    @staticmethod
    def read_all() -> list[object]:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                products = product_repository.read_all()
                if len(products) == 0:
                    raise ProductNotFoundError()
                return products
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(product_id: str) -> bool:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                product = product_repository.delete_by_id(product_id)
                if product is None:
                    raise ProductNotFoundError()
                return product
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def update(product_id: str, name: str = None, description: str = None, price: float = None,
               for_car_brand: str = None, quantity_in_stock: int = None) -> object:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                product = product_repository.update(product_id, name, description, price, for_car_brand,
                                                    quantity_in_stock)
                if product is None:
                    raise ProductNotFoundError()
                return product
        except Exception as e:
            raise e

    @staticmethod
    def update_quantity_in_stock(product_id: str, amount: int, subtract: bool = False) -> object:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                product = product_repository.update_quantity_in_stock(product_id, amount, subtract)
                if product is False:
                    raise ProductQuantityInStockSubtractionError()
                if product is None:
                    raise ProductNotFoundError()
                return product
        except Exception as e:
            raise e

    @staticmethod
    def read_products_for_car_brand(car_brand: str) -> list[object]:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                products = product_repository.read_products_for_car_brand(car_brand)
                if len(products) == 0:
                    raise ProductNotFoundError()
                return products
        except Exception as e:
            raise e

    @staticmethod
    def read_products_by_category_id(product_category_id: str) -> list[object]:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                products = product_repository.read_products_by_category_id(product_category_id)
                if len(products) == 0:
                    raise ProductNotFoundError()
                return products
        except Exception as e:
            raise e

    @staticmethod
    def read_all_products_sorted_by_price_from_lowest() -> list[object]:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                products = product_repository.read_all()
                if len(products) == 0:
                    raise ProductNotFoundError()
                keyfun = operator.attrgetter("price")
                products.sort(key=keyfun, reverse=False)
                return products
        except Exception as e:
            raise e

    @staticmethod
    def read_all_products_sorted_by_price_from_highest() -> list[object]:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                products = product_repository.read_all()
                if len(products) == 0:
                    raise ProductNotFoundError()
                keyfun = operator.attrgetter("price")
                products.sort(key=keyfun, reverse=True)
                return products
        except Exception as e:
            raise e

    @staticmethod
    def read_all_products_alphabetically_sorted() -> list[object]:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                products = product_repository.read_all()
                if len(products) == 0:
                    raise ProductNotFoundError()
                keyfun = operator.attrgetter("name")
                products.sort(key=keyfun)
                return products
        except Exception as e:
            raise e

    @staticmethod
    def read_products_name_like(name: str) -> list[object]:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                products = product_repository.read_products_name_like(name)
                if len(products) == 0:
                    raise ProductNotFoundError()
                return products
        except Exception as e:
            raise e

    @staticmethod
    def read_by_code(code: str) -> object:
        try:
            with SessionLocal() as db:
                product_repository = ProductRepository(db)
                product = product_repository.read_by_code(code)
                if product is None:
                    raise ProductCodeNotFoundError()
                return product
        except Exception as e:
            raise e
