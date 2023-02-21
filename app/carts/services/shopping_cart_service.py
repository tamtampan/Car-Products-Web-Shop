from sqlalchemy.exc import IntegrityError
from app.carts.repositories.shopping_cart_repository import ShoppingCartRepository
from app.db.database import SessionLocal
from app.carts.exceptions import ShoppingCartNotFoundError, ShoppingCartTotalCostError


class ShoppingCartService:

    @staticmethod
    def create(customer_id) -> object:
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.create(customer_id)
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(shopping_cart_id: str) -> object:
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                shopping_cart = shopping_cart_repository.read_by_id(shopping_cart_id)
                if shopping_cart is None:
                    raise ShoppingCartNotFoundError()
                return shopping_cart
        except Exception as e:
            raise e

    @staticmethod
    def read_by_customer_id(customer_id: str) -> object:
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                shopping_cart = shopping_cart_repository.read_by_customer_id(customer_id)
                if shopping_cart is None:
                    raise ShoppingCartNotFoundError()
                return shopping_cart
        except Exception as e:
            raise e

    @staticmethod
    def read_all() -> list[object]:
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                shopping_carts = shopping_cart_repository.read_all()
                if len(shopping_carts) == 0:
                    raise ShoppingCartNotFoundError()
                return shopping_carts
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(shopping_cart_id: str) -> bool:
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                shopping_cart = shopping_cart_repository.delete_by_id(shopping_cart_id)
                if shopping_cart is None:
                    raise ShoppingCartNotFoundError()
                return shopping_cart
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def update(shopping_cart_id: str, amount: float, subtract: bool = False) -> object:
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                shopping_cart = shopping_cart_repository.update(shopping_cart_id, amount, subtract)
                if shopping_cart is None:
                    raise ShoppingCartNotFoundError()
                if shopping_cart is False:
                    raise ShoppingCartTotalCostError()
                return shopping_cart
        except Exception as e:
            raise e

    @staticmethod
    def update_set_total_cost(shopping_cart_id: str, total_cost: float) -> object:
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                shopping_cart = shopping_cart_repository.update_set_total_cost(shopping_cart_id, total_cost)
                if shopping_cart is None:
                    raise ShoppingCartNotFoundError()
                return shopping_cart
        except Exception as e:
            raise e
