from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.products.models import Product
from app.products.exceptions import ProductNotFoundException, ProductQuantityInStockError


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, description: str, code: str, price: float, for_car_brand: str,
               quantity_in_stock: int, producer_id: str, product_category_id: str):
        try:
            product = Product(name, description, code, price, for_car_brand, quantity_in_stock, producer_id,
                              product_category_id)
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_by_id(self, product_id: str):
        product = self.db.query(Product).filter(Product.product_id == product_id).first()
        if product is None:
            raise ProductNotFoundException(f"Product with provided id: {product_id} not found.", 400)
        return product

    def read_all(self):
        products = self.db.query(Product).all()
        return products

    def delete_by_id(self, product_id: str):
        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            if product is None:
                raise ProductNotFoundException(f"Product with provided id: {product_id} not found.", 400)
            self.db.delete(product)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self, product_id: str, name: str = None, description: str = None, price: float = None,
               for_car_brand: str = None, quantity_in_stock: int = None):
        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            if product is None:
                raise ProductNotFoundException(f"Product with provided id: {product_id} not found.", 400)
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

    def update_quantity_in_stock(self, product_id: str, amount: int, subtract: bool = False):
        try:
            product = self.db.query(Product).filter(Product.product_id == product_id).first()
            if product is None:
                raise ProductNotFoundException(f"Product with provided id: {product_id} not found.", 400)
            if subtract:
                amount = amount * -1
            if product.quantity_in_stock + amount < 0:
                raise ProductQuantityInStockError(f"Quantity in stock can not be under 0.", 400)
            product.quantity_in_stock += amount
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except Exception as e:
            raise e
