from app.carts.repositories.cart_item_repository import CartItemRepository
from app.db.database import SessionLocal


class CartItemService:

    @staticmethod
    def create(quantity: int, shopping_cart_id: str, product_id: str):
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.create(quantity, shopping_cart_id, product_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(cart_item_id: str):
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.read_by_id(cart_item_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.read_all()
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(cart_item_id: str):
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.delete_by_id(cart_item_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_quantity(cart_item_id: str, quantity: int):
        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.update_quantity(cart_item_id, quantity)
        except Exception as e:
            raise e
