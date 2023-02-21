from sqlalchemy.orm import Session
from app.carts.models import CartItem


class CartItemRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, quantity: int, shopping_cart_id: str, product_id: str) -> object:
        try:
            cart_item = CartItem(quantity=quantity, shopping_cart_id=shopping_cart_id, product_id=product_id)
            self.db.add(cart_item)
            self.db.commit()
            self.db.refresh(cart_item)
            return cart_item
        except Exception as e:
            raise e

    def read_by_id(self, cart_item_id: str) -> object:
        try:
            cart_item = self.db.query(CartItem).filter(CartItem.cart_item_id == cart_item_id).first()
            return cart_item
        except Exception as e:
            raise e

    def read_by_shopping_cart_id(self, shopping_cart_id: str) -> list[object]:
        try:
            cart_items = self.db.query(CartItem).filter(CartItem.shopping_cart_id == shopping_cart_id).all()
            return cart_items
        except Exception as e:
            raise e

    def read_all(self) -> list[object]:
        try:
            cart_items = self.db.query(CartItem).all()
            return cart_items
        except Exception as e:
            raise e

    def delete_by_id(self, cart_item_id: str) -> bool or None:
        try:
            cart_item = self.db.query(CartItem).filter(CartItem.cart_item_id == cart_item_id).first()
            if cart_item is None:
                return None
            self.db.delete(cart_item)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_quantity(self, cart_item_id: str, quantity: int) -> object:
        try:
            cart_item = self.db.query(CartItem).filter(CartItem.cart_item_id == cart_item_id).first()
            if cart_item is None:
                return None
            cart_item.quantity = quantity
            self.db.add(cart_item)
            self.db.commit()
            self.db.refresh(cart_item)
            return cart_item
        except Exception as e:
            raise e
