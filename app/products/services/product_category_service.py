from app.products.repositories.product_category_repository import ProductCategoryRepository
from app.db.database import SessionLocal


class ProductCategoryService:

    @staticmethod
    def create(name: str):
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.create(name)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(product_category_id: str):
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.read_by_id(product_category_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.read_all()
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(product_category_id: str):
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.delete_by_id(product_category_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_name(product_category_id: str, new_name: str):
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.update_name(product_category_id, new_name)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_name(name: str):
        try:
            with SessionLocal() as db:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.read_by_name(name)
        except Exception as e:
            raise e
