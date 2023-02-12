from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.carts.models import ShoppingCart
from app.carts.exceptions import ShoppingCartNotFoundException, ShoppingCartTotalCostError


class ShoppingCartRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, customer_id: str):
        try:
            shopping_cart = ShoppingCart(total_cost=0, customer_id=customer_id)
            self.db.add(shopping_cart)
            self.db.commit()
            self.db.refresh(shopping_cart)
            return shopping_cart
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_by_id(self, shopping_cart_id: str):
        shopping_cart = self.db.query(ShoppingCart).filter(ShoppingCart.shopping_cart_id == shopping_cart_id).first()
        if shopping_cart is None:
            raise ShoppingCartNotFoundException(f"Shopping cart with provided id: {shopping_cart_id} not found.", 400)
        return shopping_cart

    def read_all(self):
        shopping_cart = self.db.query(ShoppingCart).all()
        return shopping_cart

    def delete_by_id(self, shopping_cart_id: str):
        try:
            shopping_cart = \
                self.db.query(ShoppingCart).filter(ShoppingCart.shopping_cart_id == shopping_cart_id).first()
            if shopping_cart is None:
                raise ShoppingCartNotFoundException(f"Shopping cart with provided id: "
                                                    f"{shopping_cart_id} not found.", 400)
            self.db.delete(shopping_cart)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self, shopping_cart_id: str, amount: float, subtract: bool = False):
        try:
            shopping_cart = \
                self.db.query(ShoppingCart).filter(ShoppingCart.shopping_cart_id == shopping_cart_id).first()
            if shopping_cart is None:
                raise ShoppingCartNotFoundException \
                    (f"Shopping cart with provided id: {shopping_cart_id} not found.", 400)
            if subtract:
                amount = amount * -1
            if shopping_cart.total_cost + amount < 0:
                raise ShoppingCartTotalCostError(f"Total cost can not be under 0", 400)
            shopping_cart.total_cost += amount
            self.db.add(shopping_cart)
            self.db.commit()
            self.db.refresh(shopping_cart)
            return shopping_cart
        except Exception as e:
            raise e
