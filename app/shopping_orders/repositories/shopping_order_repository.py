from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.shopping_orders.models import ShoppingOrder
from app.shopping_orders.exceptions import ShoppingOrderNotFoundException


class ShoppingOrderRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, total_price: float, status: int, order_date: str, shipped_date: str, customer_id: str,
               office_id: str):
        try:
            shopping_order = ShoppingOrder(total_price, status, order_date, shipped_date, customer_id, office_id)
            self.db.add(shopping_order)
            self.db.commit()
            self.db.refresh(shopping_order)
            return shopping_order
        except Exception as e:
            raise e

    def read_by_id(self, shopping_order_id: str):
        shopping_order = self.db.query(ShoppingOrder).filter\
            (ShoppingOrder.shopping_order_id == shopping_order_id).first()
        if shopping_order is None:
            raise ShoppingOrderNotFoundException(f"Shopping order with provided id: "
                                                 f"{shopping_order_id} not found.", 400)
        return shopping_order

    def read_all(self):
        shopping_orders = self.db.query(ShoppingOrder).all()
        return shopping_orders

    def delete_by_id(self, shopping_order_id: str):
        try:
            shopping_order = self.db.query(ShoppingOrder).filter\
                (ShoppingOrder.shopping_order_id == shopping_order_id).first()
            if shopping_order is None:
                raise ShoppingOrderNotFoundException\
                    (f"Shopping order with provided id: {shopping_order_id} not found.", 400)
            self.db.delete(shopping_order)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self, shopping_order_id: str, status: int = None, shipped_date: str = None):
        try:
            shopping_order = self.db.query(ShoppingOrder).filter\
                (ShoppingOrder.shopping_order_id == shopping_order_id).first()
            if shopping_order is None:
                raise ShoppingOrderNotFoundException\
                    (f"Shopping order with provided id: {shopping_order_id} not found.", 400)
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
