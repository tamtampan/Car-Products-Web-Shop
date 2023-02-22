from app.db.database import SessionLocal
from app.shopping_orders.exceptions import ShoppingOrderItemNotFoundError
from app.shopping_orders.repositories import ShoppingOrderItemRepository


class ShoppingOrderItemService:
    """Shopping Order Item Service"""

    @staticmethod
    def create(quantity: int, product_id: str, shopping_order_id: str) -> object:
        try:
            with SessionLocal() as db:
                shopping_order_item_repository = ShoppingOrderItemRepository(db)
                return shopping_order_item_repository.create(quantity, product_id, shopping_order_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(shopping_order_item_id: str) -> object:
        try:
            with SessionLocal() as db:
                shopping_order_item_repository = ShoppingOrderItemRepository(db)
                shopping_order_item = shopping_order_item_repository.read_by_id(shopping_order_item_id)
                if shopping_order_item is None:
                    raise ShoppingOrderItemNotFoundError()
                return shopping_order_item
        except Exception as e:
            raise e

    @staticmethod
    def read_all() -> list[object]:
        try:
            with SessionLocal() as db:
                shopping_order_item_repository = ShoppingOrderItemRepository(db)
                shopping_orders = shopping_order_item_repository.read_all()
                if len(shopping_orders) == 0:
                    raise ShoppingOrderItemNotFoundError()
                return shopping_orders
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(shopping_order_item_id: str) -> bool:
        try:
            with SessionLocal() as db:
                shopping_order_item_repository = ShoppingOrderItemRepository(db)
                shopping_order_item = shopping_order_item_repository.delete_by_id(shopping_order_item_id)
                if shopping_order_item is None:
                    raise ShoppingOrderItemNotFoundError()
                return shopping_order_item
        except Exception as e:
            raise e

    @staticmethod
    def read_items_by_shopping_order_id(shopping_order_id: str) -> list[object]:
        try:
            with SessionLocal() as db:
                shopping_order_item_repository = ShoppingOrderItemRepository(db)
                shopping_order_items = shopping_order_item_repository.read_items_by_shopping_order_id(shopping_order_id)
                if len(shopping_order_items) == 0:
                    raise ShoppingOrderItemNotFoundError()
                return shopping_order_items
        except Exception as e:
            raise e
