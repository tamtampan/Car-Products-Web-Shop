"""Cart Item Service"""

from app.carts.exceptions import CartItemNotFoundError, QuantityNotValid
from app.carts.repositories.cart_item_repository import CartItemRepository
from app.db.database import SessionLocal


class CartItemService:
    """Cart Item Service"""

    @staticmethod
    def create(quantity: int, shopping_cart_id: str, product_id: str) -> object:
        """Create Cart Item"""

        try:
            if quantity < 1 or quantity > 20:
                raise QuantityNotValid()
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                return cart_item_repository.create(quantity, shopping_cart_id, product_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(cart_item_id: str) -> object:
        """Read by id"""

        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                cart_item = cart_item_repository.read_by_id(cart_item_id)
                if cart_item is None:
                    raise CartItemNotFoundError()
                return cart_item
        except Exception as e:
            raise e

    @staticmethod
    def read_all() -> list[object]:
        """Read all"""

        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                cart_items = cart_item_repository.read_all()
                if len(cart_items) == 0:
                    raise CartItemNotFoundError()
                return cart_items
        except Exception as e:
            raise e

    @staticmethod
    def read_by_shopping_cart_id(shopping_cart_id: str) -> list[object]:
        """Read by shopping cart id"""

        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                cart_items = cart_item_repository.read_by_shopping_cart_id(shopping_cart_id)
                if len(cart_items) == 0:
                    raise CartItemNotFoundError()
                return cart_items
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(cart_item_id: str) -> bool:
        """Delete by id"""

        try:
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                cart_item = cart_item_repository.delete_by_id(cart_item_id)
                if cart_item is None:
                    raise CartItemNotFoundError()
                return cart_item
        except Exception as e:
            raise e

    @staticmethod
    def update_quantity(cart_item_id: str, quantity: int) -> object:
        """Update quantity"""

        try:
            if quantity < 1 or quantity > 20:
                raise QuantityNotValid()
            with SessionLocal() as db:
                cart_item_repository = CartItemRepository(db)
                cart_item = cart_item_repository.update_quantity(cart_item_id, quantity)
                if cart_item is None:
                    raise CartItemNotFoundError()
                return cart_item
        except Exception as e:
            raise e
