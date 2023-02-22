"""Product Repository"""

from sqlalchemy.orm import Session

from app.products.models import Product


class ProductRepository:
    """Product Repository"""

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        name: str,
        description: str,
        code: str,
        price: float,
        for_car_brand: str,
        quantity_in_stock: int,
        producer_id: str,
        product_category_id: str,
    ) -> object:
        """Create Product"""

        try:
            product = Product(
                name, description, code, price, for_car_brand, quantity_in_stock, producer_id, product_category_id
            )
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except Exception as e:
            raise e

    def read_by_id(self, product_id: str) -> object:
        """Read by id"""

        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            return product
        except Exception as e:
            raise e

    def read_all(self) -> list[object]:
        """Read all"""

        try:
            products = self.db.query(Product).all()
            return products
        except Exception as e:
            raise e

    def delete_by_id(self, product_id: str) -> bool or None:
        """Delete by id"""

        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            if product is None:
                return None
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(
        self,
        product_id: str,
        name: str = None,
        description: str = None,
        price: float = None,
        for_car_brand: str = None,
        quantity_in_stock: int = None,
    ) -> object:
        """Update"""

        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            if product is None:
                return None
            if name is not None:
                product.name = name
            if description is not None:
                product.description = description
            if price is not None:
                product.price = price
            if for_car_brand is not None:
                product.for_car_brand = for_car_brand
            if quantity_in_stock is not None:
                product.quantity_in_stock = quantity_in_stock
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except Exception as e:
            raise e

    def update_quantity_in_stock(self, product_id: str, amount: int, subtract: bool = False) -> object:
        """Update quantity in stock"""

        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            if product is None:
                return None
            if subtract:
                amount = amount * -1
            if product.quantity_in_stock + amount < 0:
                return False
            product.quantity_in_stock += amount
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except Exception as e:
            raise e

    def read_products_for_car_brand(self, car_brand: str) -> list[object]:
        """Read all for car brand"""

        try:
            products = self.db.query(Product).filter(Product.for_car_brand.ilike(f"{car_brand}%")).all()
            return products
        except Exception as e:
            raise e

    def read_products_by_category_id(self, product_category_id: str) -> list[object]:
        """Read by category id"""

        try:
            products = self.db.query(Product).filter(Product.product_category_id == product_category_id).all()
            return products
        except Exception as e:
            raise e

    def read_products_name_like(self, name: str) -> list[object]:
        """Read by name"""

        try:
            products = self.db.query(Product).filter(Product.name.ilike(f"{name}%")).all()
            return products
        except Exception as e:
            raise e

    def read_by_code(self, code: str) -> object:
        """Read by code"""

        try:
            product = self.db.query(Product).filter(Product.code == code).first()
            return product
        except Exception as e:
            raise e
