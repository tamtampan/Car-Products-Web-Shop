from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.products.models import ProductCategory
from app.products.exceptions import ProductCategoryNotFoundException


class ProductCategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name):
        try:
            product_category = ProductCategory(name)
            self.db.add(product_category)
            self.db.commit()
            self.db.refresh(product_category)
            return product_category
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_by_id(self, product_category_id: str):
        product_category = self.db.query(ProductCategory).filter(ProductCategory.product_category_id ==
                                                                 product_category_id).first()
        if product_category is None:
            raise ProductCategoryNotFoundException\
                (f"Product category with provided id: {product_category_id} not found.", 400)
        return product_category

    def read_by_name(self, name: str):
        product_category = self.db.query(ProductCategory).filter(ProductCategory.name == name).first()
        if product_category is None:
            raise ProductCategoryNotFoundException(f"Product category with provided name: {name} not found.", 400)
        return product_category

    def read_all(self):
        product_categories = self.db.query(ProductCategory).all()
        return product_categories

    def delete_by_id(self, product_category_id: str):
        try:
            product_category = self.db.query(ProductCategory).filter(ProductCategory.product_category_id ==
                                                                     product_category_id).first()
            if product_category is None:
                raise ProductCategoryNotFoundException \
                    (f"Product category with provided id: {product_category_id} not found.", 400)
            self.db.delete(product_category)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_name(self, product_category_id: str, new_name: str):
        try:
            product_category = self.db.query(ProductCategory).filter(ProductCategory.product_category_id ==
                                                                     product_category_id).first()
            if product_category is None:
                raise ProductCategoryNotFoundException \
                    (f"Product category with provided id: {product_category_id} not found.", 400)
            product_category.name = new_name
            self.db.add(product_category)
            self.db.commit()
            self.db.refresh(product_category)
            return product_category
        except Exception as e:
            raise e
