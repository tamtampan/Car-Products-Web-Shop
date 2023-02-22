"""Cart Item Repository"""

from sqlalchemy.orm import Session

from app.carts.models import CartItem


class CartItemRepository:
    """Cart Item Repository"""

    def __init__(self, db: Session):
        self.db = db

    def create(self, quantity: int, shopping_cart_id: str, product_id: str) -> object:
        """Create Cart Item"""
        try:
            cart_item = CartItem(quantity=quantity, shopping_cart_id=shopping_cart_id, product_id=product_id)
            self.db.add(cart_item)
            self.db.commit()
            self.db.refresh(cart_item)
            return cart_item
        except Exception as e:
            raise e

    def read_by_id(self, cart_item_id: str) -> object:
        """Read by id"""
        try:
            cart_item = self.db.query(CartItem).filter(CartItem.cart_item_id == cart_item_id).first()
            return cart_item
        except Exception as e:
            raise e

    def read_by_shopping_cart_id(self, shopping_cart_id: str) -> list[object]:
        """Read by shopping cart id"""

        try:
            cart_items = self.db.query(CartItem).filter(CartItem.shopping_cart_id == shopping_cart_id).all()
            return cart_items
        except Exception as e:
            raise e

    def read_all(self) -> list[object]:
        """Read all"""

        try:
            cart_items = self.db.query(CartItem).all()
            return cart_items
        except Exception as e:
            raise e

    def delete_by_id(self, cart_item_id: str) -> bool or None:
        """Delete by id"""

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
        """Update quantity"""

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
