from app.carts.repositories.shopping_cart_repository import ShoppingCartRepository
from app.db.database import SessionLocal



from sqlalchemy.exc import IntegrityError


class ShoppingCartService:

    @staticmethod
    def create(customer_id):
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.create(customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(shopping_cart_id: str):
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.read_by_id(shopping_cart_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.read_all()
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(shopping_cart_id: str):
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.delete_by_id(shopping_cart_id)
        except Exception as e:
            raise e

    @staticmethod
    def update(shopping_cart_id: str, amount: float, subtract: bool = False):
        try:
            with SessionLocal() as db:
                shopping_cart_repository = ShoppingCartRepository(db)
                return shopping_cart_repository.update(shopping_cart_id, amount, subtract)
        except Exception as e:
            raise e
