from sqlalchemy.orm import Session
from app.products.models import ProductCategory


class ProductCategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name) -> object:
        try:
            product_category = ProductCategory(name)
            self.db.add(product_category)
            self.db.commit()
            self.db.refresh(product_category)
            return product_category
        except Exception as e:
            raise e

    def read_by_id(self, product_category_id: str) -> object:
        try:
            product_category = self.db.query(ProductCategory).filter(ProductCategory.product_category_id ==
                                                                     product_category_id).first()
            return product_category
        except Exception as e:
            raise e

    def read_by_name(self, name: str) -> object:
        try:
            product_category = self.db.query(ProductCategory).filter(ProductCategory.name == name).first()
            return product_category
        except Exception as e:
            raise e

    def read_all(self) -> list[object]:
        try:
            product_categories = self.db.query(ProductCategory).all()
            return product_categories
        except Exception as e:
            raise e

    def delete_by_id(self, product_category_id: str) -> bool or None:
        try:
            product_category = self.db.query(ProductCategory).filter(ProductCategory.product_category_id ==
                                                                     product_category_id).first()
            if product_category is None:
                return None
            self.db.delete(product_category)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_name(self, product_category_id: str, new_name: str) -> object:
        try:
            product_category = self.db.query(ProductCategory).filter(ProductCategory.product_category_id ==
                                                                     product_category_id).first()
            if product_category is None:
                return None
            product_category.name = new_name
            self.db.add(product_category)
            self.db.commit()
            self.db.refresh(product_category)
            return product_category
        except Exception as e:
            raise e

    def read_category_name_like(self, name: str) -> object:
        try:
            product_category = self.db.query(ProductCategory).filter(ProductCategory.name.ilike(f"%{name}%")).first()
            return product_category
        except Exception as e:
            raise e
