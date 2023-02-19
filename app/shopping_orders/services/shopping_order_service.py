from app.shopping_orders.repositories import ShoppingOrderRepository
from sqlalchemy.exc import IntegrityError
from app.shopping_orders.exceptions import ShoppingOrderNotFoundError, ShoppingOrderTotalPriceSubtractionError
from app.db.database import SessionLocal
from datetime import date


class ShoppingOrderService:

    @staticmethod
    def create(total_price: float, shipping_cost: float, status: int, order_date: str, shipped_date: str,
               customer_id: str, office_id: str) -> object:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                return shopping_order_repository.create(total_price, shipping_cost, status, order_date, shipped_date,
                                                        customer_id, office_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(shopping_order_id: str) -> object:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_order = shopping_order_repository.read_by_id(shopping_order_id)
                if shopping_order is None:
                    raise ShoppingOrderNotFoundError()
                return shopping_order
        except Exception as e:
            raise e

    @staticmethod
    def read_all() -> list[object]:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                return shopping_order_repository.read_all()
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(shopping_order_id: str) -> bool:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_order = shopping_order_repository.delete_by_id(shopping_order_id)
                if shopping_order is None:
                    raise ShoppingOrderNotFoundError()
                return shopping_order
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def update(shopping_order_id: str, shipping_cost: float = None, status: int = None,
               shipped_date: str = None) -> object:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_order = shopping_order_repository.update\
                    (shopping_order_id, shipping_cost, status, shipped_date)
                if shopping_order is None:
                    raise ShoppingOrderNotFoundError()
                return shopping_order
        except Exception as e:
            raise e

    @staticmethod
    def read_today_shopping_orders() -> list[object]:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                return shopping_order_repository.read_today_shopping_orders()
        except Exception as e:
            raise e

    @staticmethod
    def update_total_price(shopping_order_id: str, total_price: float) -> object:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_order = shopping_order_repository.update_total_price(shopping_order_id, total_price)
                if shopping_order is None:
                    raise ShoppingOrderNotFoundError()
                return shopping_order
        except Exception as e:
            raise e

    @staticmethod
    def sum_today_profit() -> float:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_orders = shopping_order_repository.read_today_shopping_orders()
                profit = 0
                for order in shopping_orders:
                    profit += order.total_price
                return profit
        except Exception as e:
            raise e

    @staticmethod
    def update_total_price_for_amount(shopping_order_id: str, amount: float, subtract: bool = False) -> object:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_order = shopping_order_repository.update_total_price_for_amount\
                    (shopping_order_id, amount, subtract)
                if shopping_order is False:
                    raise ShoppingOrderTotalPriceSubtractionError()
                if shopping_order is None:
                    raise ShoppingOrderNotFoundError()
                return shopping_order
        except Exception as e:
            raise e
