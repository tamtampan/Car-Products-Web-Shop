from sqlalchemy.orm import Session
from app.carts.models import ShoppingCart


class ShoppingCartRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, customer_id: str) -> object:
        try:
            shopping_cart = ShoppingCart(customer_id)
            self.db.add(shopping_cart)
            self.db.commit()
            self.db.refresh(shopping_cart)
            return shopping_cart
        except Exception as e:
            raise e

    def read_by_id(self, shopping_cart_id: str) -> object:
        try:
            shopping_cart = self.db.query(ShoppingCart).filter\
                (ShoppingCart.shopping_cart_id == shopping_cart_id).first()
            return shopping_cart
        except Exception as e:
            raise e

    def read_all(self) -> list[object]:
        try:
            shopping_carts = self.db.query(ShoppingCart).all()
            return shopping_carts
        except Exception as e:
            raise e

    def delete_by_id(self, shopping_cart_id: str) -> bool or None:
        try:
            shopping_cart = \
                self.db.query(ShoppingCart).filter(ShoppingCart.shopping_cart_id == shopping_cart_id).first()
            if shopping_cart is None:
                return None
            self.db.delete(shopping_cart)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self, shopping_cart_id: str, amount: float, subtract: bool = False) -> object:
        try:
            shopping_cart = \
                self.db.query(ShoppingCart).filter(ShoppingCart.shopping_cart_id == shopping_cart_id).first()
            if shopping_cart is None:
                return None
            if subtract:
                amount = amount * -1
            if shopping_cart.total_cost + amount < 0:
                return False
            shopping_cart.total_cost += amount
            self.db.add(shopping_cart)
            self.db.commit()
            self.db.refresh(shopping_cart)
            return shopping_cart
        except Exception as e:
            raise e
