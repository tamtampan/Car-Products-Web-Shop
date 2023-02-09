from app.products.repositories.product_category_repository import ProductCategoryRepository
from app.db.database import SessionLocal


class ProductCategoryService:

    @staticmethod
    def create(name):
        with SessionLocal() as db:
            try:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.create(name)
            except Exception as e:
                raise e

    @staticmethod
    def get_by_id(product_category_id: str):
        with SessionLocal() as db:
            product_category_repository = ProductCategoryRepository(db)
            return product_category_repository.read_by_id(product_category_id)

    @staticmethod
    def get_all():
        with SessionLocal() as db:
            product_category_repository = ProductCategoryRepository(db)
            return product_category_repository.read_all()

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
        with SessionLocal() as db:
            try:
                product_category_repository = ProductCategoryRepository(db)
                return product_category_repository.update_name(product_category_id, new_name)
            except Exception as e:
                raise e

    @staticmethod
    def get_by_name(name: str):
        with SessionLocal() as db:
            product_category_repository = ProductCategoryRepository(db)
            return product_category_repository.read_by_name(name)
