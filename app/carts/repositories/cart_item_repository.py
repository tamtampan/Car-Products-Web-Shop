from sqlalchemy.orm import Session
from app.carts.models import CartItem
from app.carts.exceptions import CartItemNotFoundException


class CartItemRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, quantity: int, shopping_cart_id: str, product_id: str):
        try:
            cart_item = CartItem(quantity=quantity, shopping_cart_id=shopping_cart_id, product_id=product_id)
            self.db.add(cart_item)
            self.db.commit()
            self.db.refresh(cart_item)
            return cart_item
        except Exception as e:
            raise e

    def read_by_id(self, cart_item_id: str):
        cart_item = self.db.query(CartItem).filter(CartItem.cart_item_id == cart_item_id).first()
        if cart_item is None:
            raise CartItemNotFoundException(f"Cart item with provided id: {cart_item_id} not found.", 400)
        return cart_item

    def read_all(self):
        cart_items = self.db.query(CartItem).all()
        return cart_items

    def delete_by_id(self, cart_item_id: str):
        try:
            cart_item = self.db.query(CartItem).filter(CartItem.cart_item_id == cart_item_id).first()
            if cart_item is None:
                raise CartItemNotFoundException(f"Cart item with provided id - {cart_item_id} not found.", 400)
            self.db.delete(cart_item)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_quantity(self, cart_item_id: str, quantity: int):
        try:
            cart_item = self.db.query(CartItem).filter(CartItem.cart_item_id == cart_item_id).first()
            if cart_item is None:
                raise CartItemNotFoundException(f"Cart item with provided id: {cart_item_id} not found.", 400)
            cart_item.quantity = quantity
            self.db.add(cart_item)
            self.db.commit()
            self.db.refresh(cart_item)
            return cart_item
        except Exception as e:
            raise e
