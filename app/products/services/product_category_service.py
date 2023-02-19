from app.products.repositories.product_category_repository import ProductCategoryRepository
from app.db.database import SessionLocal
from app.products.exceptions import ProductCategoryNotFoundError
from sqlalchemy.exc import IntegrityError


class ProductCategoryService:

    @staticmethod
    def create(name: str) -> object:
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.create(name)
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(product_category_id: str) -> object:
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                product_category = product_category_repository.read_by_id(product_category_id)
                if product_category is None:
                    raise ProductCategoryNotFoundError()
                return product_category
        except Exception as e:
            raise e

    @staticmethod
    def read_all() -> list[object]:
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.read_all()
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(product_category_id: str) -> bool:
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                product_category = product_category_repository.delete_by_id(product_category_id)
                if product_category is None:
                    raise ProductCategoryNotFoundError()
                return product_category
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def update_name(product_category_id: str, new_name: str) -> object:
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                product_category = product_category_repository.update_name(product_category_id, new_name)
                if product_category is None:
                    raise ProductCategoryNotFoundError()
                return product_category
        except Exception as e:
            raise e

    @staticmethod
    def read_by_name(name: str) -> object:
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                product_category = product_category_repository.read_by_name(name)
                if product_category is None:
                    raise ProductCategoryNotFoundError()
                return product_category
        except Exception as e:
            raise e

    @staticmethod
    def read_category_name_like(name: str) -> object:
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                product_category = product_category_repository.read_category_name_like(name)
                if product_category is None:
                    raise ProductCategoryNotFoundError()
                return product_category
        except Exception as e:
            raise e
