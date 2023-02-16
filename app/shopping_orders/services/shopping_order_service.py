from app.shopping_orders.repositories import ShoppingOrderRepository
from app.db.database import SessionLocal


class ShoppingOrderService:

    @staticmethod
    def create(total_price: float, status: int, order_date: str, shipped_date: str, customer_id: str, office_id: str):
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                return shopping_order_repository.create(total_price, status, order_date, shipped_date,
                                                        customer_id, office_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(shopping_order_id: str):
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                return shopping_order_repository.read_by_id(shopping_order_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                return shopping_order_repository.read_all()
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(shopping_order_id: str):
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                return shopping_order_repository.delete_by_id(shopping_order_id)
        except Exception as e:
            raise e

    @staticmethod
    def update(shopping_order_id: str, status: int = None, shipped_date: str = None):
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                return shopping_order_repository.update(shopping_order_id, status, shipped_date)
        except Exception as e:
            raise e
