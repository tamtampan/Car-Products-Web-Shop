from sqlalchemy.orm import Session

from app.shopping_orders.models import ShoppingOrderItem


class ShoppingOrderItemRepository:
    """Shopping Order Item Repository"""

    def __init__(self, db: Session):
        self.db = db

    def create(self, quantity: int, product_id: str, shopping_order_id: str) -> object:
        try:
            shopping_order_item = ShoppingOrderItem(quantity, product_id, shopping_order_id)
            self.db.add(shopping_order_item)
            self.db.commit()
            self.db.refresh(shopping_order_item)
            return shopping_order_item
        except Exception as e:
            raise e

    def read_by_id(self, shopping_order_item_id: str) -> object:
        try:
            shopping_order_item = (
                self.db.query(ShoppingOrderItem)
                .filter(ShoppingOrderItem.shopping_order_item_id == shopping_order_item_id)
                .first()
            )
            return shopping_order_item
        except Exception as e:
            raise e

    def read_all(self) -> list[object]:
        try:
            shopping_order_items = self.db.query(ShoppingOrderItem).all()
            return shopping_order_items
        except Exception as e:
            raise e

    def delete_by_id(self, shopping_order_item_id: str) -> bool or None:
        try:
            shopping_order_item = (
                self.db.query(ShoppingOrderItem)
                .filter(ShoppingOrderItem.shopping_order_item_id == shopping_order_item_id)
                .first()
            )
            if shopping_order_item is None:
                return None
            self.db.delete(shopping_order_item)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def read_items_by_shopping_order_id(self, shopping_order_id: str) -> list[object]:
        try:
            shopping_order_items = (
                self.db.query(ShoppingOrderItem).filter(ShoppingOrderItem.shopping_order_id == shopping_order_id).all()
            )
            return shopping_order_items
        except Exception as e:
            raise e
