from datetime import date

from sqlalchemy.orm import Session

from app.shopping_orders.models import ShoppingOrder


class ShoppingOrderRepository:
    """Shopping Order Repository"""

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        total_price: float,
        shipping_cost: float,
        status: int,
        order_date: str,
        shipped_date: str or None,
        customer_id: str,
        office_id: str,
    ) -> object:
        try:
            shopping_order = ShoppingOrder(
                total_price, shipping_cost, order_date, shipped_date, customer_id, office_id, status
            )
            self.db.add(shopping_order)
            self.db.commit()
            self.db.refresh(shopping_order)
            return shopping_order
        except Exception as e:
            raise e

    def read_by_id(self, shopping_order_id: str) -> object:
        try:
            shopping_order = (
                self.db.query(ShoppingOrder).filter(ShoppingOrder.shopping_order_id == shopping_order_id).first()
            )
            return shopping_order
        except Exception as e:
            raise e

    def read_all(self) -> list[object]:
        try:
            shopping_orders = self.db.query(ShoppingOrder).all()
            return shopping_orders
        except Exception as e:
            raise e

    def delete_by_id(self, shopping_order_id: str) -> bool or None:
        try:
            shopping_order = (
                self.db.query(ShoppingOrder).filter(ShoppingOrder.shopping_order_id == shopping_order_id).first()
            )
            if shopping_order is None:
                return None
            self.db.delete(shopping_order)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(
        self, shopping_order_id: str, shipping_cost: float = None, status: int = None, shipped_date: str = None
    ) -> object:
        try:
            shopping_order = (
                self.db.query(ShoppingOrder).filter(ShoppingOrder.shopping_order_id == shopping_order_id).first()
            )
            if shopping_order is None:
                return None
            if shipping_cost is not None:
                shopping_order.shipping_cost = shipping_cost
            if status is not None:
                shopping_order.status = status
            if shipped_date is not None:
                shopping_order.shipped_date = shipped_date
            self.db.add(shopping_order)
            self.db.commit()
            self.db.refresh(shopping_order)
            return shopping_order
        except Exception as e:
            raise e

    def read_today_shopping_orders(self) -> list[object]:
        try:
            shopping_orders = self.db.query(ShoppingOrder).filter(ShoppingOrder.order_date == date.today()).all()
            return shopping_orders
        except Exception as e:
            raise e

    def update_total_price(self, shopping_order_id: str, total_price: float) -> object:
        try:
            shopping_order = (
                self.db.query(ShoppingOrder).filter(ShoppingOrder.shopping_order_id == shopping_order_id).first()
            )
            if shopping_order is None:
                return None
            shopping_order.total_price = total_price
            self.db.add(shopping_order)
            self.db.commit()
            self.db.refresh(shopping_order)
            return shopping_order
        except Exception as e:
            raise e

    def update_total_price_for_amount(self, shopping_order_id: str, amount: float, subtract: bool = False) -> object:
        try:
            shopping_order = (
                self.db.query(ShoppingOrder).filter(ShoppingOrder.shopping_order_id == shopping_order_id).first()
            )
            if shopping_order is None:
                return None
            if subtract:
                amount = amount * -1
            if shopping_order.total_price + amount < 0:
                return False
            shopping_order.total_price += amount
            self.db.add(shopping_order)
            self.db.commit()
            self.db.refresh(shopping_order)
            return shopping_order
        except Exception as e:
            raise e
