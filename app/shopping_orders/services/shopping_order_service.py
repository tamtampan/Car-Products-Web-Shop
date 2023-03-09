from datetime import datetime

from sqlalchemy.exc import IntegrityError

from app.db.database import SessionLocal
from app.shopping_orders.exceptions import (
    DateNotValid,
    ShoppingOrderNotFoundError,
    ShoppingOrderTotalPriceSubtractionError,
)
from app.shopping_orders.repositories import ShoppingOrderRepository


class ShoppingOrderService:
    """Shopping Order Service"""

    @staticmethod
    def valid_date(date_str: str) -> bool:
        earl_date = datetime.strptime("2020-01-01", "%Y-%m-%d")
        late_date = datetime.strptime("2030-01-01", "%Y-%m-%d")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if earl_date > date or date > late_date:
            return False
        else:
            return True

    @staticmethod
    def create(
        total_price: float,
        shipping_cost: float,
        status: int,
        order_date: str,
        shipped_date: str or None,
        customer_id: str,
        office_id: str,
    ) -> object:
        try:
            if ShoppingOrderService.valid_date(order_date):
                if shipped_date is not None:
                    if ShoppingOrderService.valid_date(shipped_date):
                        if datetime.strptime(order_date, "%Y-%m-%d") > datetime.strptime(shipped_date, "%Y-%m-%d"):
                            raise DateNotValid("Shipped date can not be before order date.")
                    else:
                        raise DateNotValid("Shipped date not valid. Should be after 2020-01-01 and before 2030-01-01.")
            else:
                raise DateNotValid("Order date not valid. Should be after 2020-01-01 and before 2030-01-01.")
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                return shopping_order_repository.create(
                    total_price, shipping_cost, status, order_date, shipped_date, customer_id, office_id
                )
        except Exception as exc:
            raise exc

    @staticmethod
    def read_by_id(shopping_order_id: str) -> object:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_order = shopping_order_repository.read_by_id(shopping_order_id)
                if shopping_order is None:
                    raise ShoppingOrderNotFoundError()
                return shopping_order
        except Exception as exc:
            raise exc

    @staticmethod
    def read_all() -> list[object]:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_orders = shopping_order_repository.read_all()
                if len(shopping_orders) == 0:
                    raise ShoppingOrderNotFoundError()
                return shopping_orders
        except Exception as exc:
            raise exc

    @staticmethod
    def delete_by_id(shopping_order_id: str) -> bool:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_order = shopping_order_repository.delete_by_id(shopping_order_id)
                if shopping_order is None:
                    raise ShoppingOrderNotFoundError()
                return shopping_order
        except IntegrityError as exc:
            raise exc
        except Exception as exc:
            raise exc

    @staticmethod
    def update(
        shopping_order_id: str, shipping_cost: float = None, status: int = None, shipped_date: str = None
    ) -> object:
        try:
            if shipped_date is not None:
                if not ShoppingOrderService.valid_date(shipped_date):
                    raise DateNotValid("Shipped date not valid. Should be after 2020-01-01 and before 2030-01-01.")
            with SessionLocal() as db:
                if shipped_date is not None:
                    shopping_order_repository = ShoppingOrderRepository(db)
                    old_shopping_order = shopping_order_repository.read_by_id(shopping_order_id)
                    if old_shopping_order is None:
                        raise ShoppingOrderNotFoundError()
                    if datetime.strptime(str(old_shopping_order.order_date), "%Y-%m-%d") > datetime.strptime(
                        shipped_date, "%Y-%m-%d"
                    ):
                        raise DateNotValid("Shipped date can not be before order date.")
                shopping_order = shopping_order_repository.update(
                    shopping_order_id, shipping_cost, status, shipped_date
                )
                return shopping_order
        except ValueError as exc:
            raise exc
        except Exception as exc:
            raise exc

    @staticmethod
    def read_today_shopping_orders() -> list[object]:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_orders = shopping_order_repository.read_today_shopping_orders()
                if len(shopping_orders) == 0:
                    raise ShoppingOrderNotFoundError()
                return shopping_orders
        except Exception as exc:
            raise exc

    @staticmethod
    def update_total_price(shopping_order_id: str, total_price: float) -> object:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_order = shopping_order_repository.update_total_price(shopping_order_id, total_price)
                if shopping_order is None:
                    raise ShoppingOrderNotFoundError()
                return shopping_order
        except Exception as exc:
            raise exc

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
        except Exception as exc:
            raise exc

    @staticmethod
    def update_total_price_for_amount(shopping_order_id: str, amount: float, subtract: bool = False) -> object:
        try:
            with SessionLocal() as db:
                shopping_order_repository = ShoppingOrderRepository(db)
                shopping_order = shopping_order_repository.update_total_price_for_amount(
                    shopping_order_id, amount, subtract
                )
                if shopping_order is False:
                    raise ShoppingOrderTotalPriceSubtractionError()
                if shopping_order is None:
                    raise ShoppingOrderNotFoundError()
                return shopping_order
        except Exception as exc:
            raise exc
