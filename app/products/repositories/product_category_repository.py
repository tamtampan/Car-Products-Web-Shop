"""Product Category Repository"""

from sqlalchemy.orm import Session

from app.products.models import ProductCategory


class ProductCategoryRepository:
    """Product Category Repository"""

    def __init__(self, db: Session):
        self.db = db

    def create(self, name) -> object:
        """Create"""

        try:
            product_category = ProductCategory(name)
            self.db.add(product_category)
            self.db.commit()
            self.db.refresh(product_category)
            return product_category
        except Exception as exc:
            raise exc

    def read_by_id(self, product_category_id: str) -> object:
        """Read by id"""

        try:
            product_category = (
                self.db.query(ProductCategory)
                .filter(ProductCategory.product_category_id == product_category_id)
                .first()
            )
            return product_category
        except Exception as exc:
            raise exc

    def read_by_name(self, name: str) -> object:
        """Read by name"""

        try:
            product_category = self.db.query(ProductCategory).filter(ProductCategory.name == name).first()
            return product_category
        except Exception as exc:
            raise exc

    def read_all(self) -> list[object]:
        """Read all"""

        try:
            product_categories = self.db.query(ProductCategory).all()
            return product_categories
        except Exception as exc:
            raise exc

    def delete_by_id(self, product_category_id: str) -> bool or None:
        """Delete by id"""

        try:
            product_category = (
                self.db.query(ProductCategory)
                .filter(ProductCategory.product_category_id == product_category_id)
                .first()
            )
            if product_category is None:
                return None
            self.db.delete(product_category)
            self.db.commit()
            return True
        except Exception as exc:
            raise exc

    def update_name(self, product_category_id: str, new_name: str) -> object:
        """Update name"""

        try:
            product_category = (
                self.db.query(ProductCategory)
                .filter(ProductCategory.product_category_id == product_category_id)
                .first()
            )
            if product_category is None:
                return None
            product_category.name = new_name
            self.db.add(product_category)
            self.db.commit()
            self.db.refresh(product_category)
            return product_category
        except Exception as exc:
            raise exc

    def read_category_name_like(self, name: str) -> object:
        """Read category name by initial letters"""

        try:
            product_category = self.db.query(ProductCategory).filter(ProductCategory.name.ilike(f"%{name}%")).first()
            return product_category
        except Exception as exc:
            raise exc
