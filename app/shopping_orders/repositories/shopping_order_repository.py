from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.shopping_orders.models import ShoppingOrder
from app.shopping_orders.exceptions import ShoppingOrderNotFoundException


class ShoppingOrderRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, total_price: float, status: int, order_date: date, shipped_date: date, customer_id: str,
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
            raise ShoppingOrderNotFoundException(f"Shopping Order with provided id: "
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
                    (f"Shopping Order with provided id: {shopping_order_id} not found.", 400)
            self.db.delete(shopping_order)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self, shopping_order_id, total_price: float, status: int, order_date: date, shipped_date: date, customer_id: str,
               office_id: str):
        try:
            shopping_order = self.db.query(ShoppingOrder).filter\
                (ShoppingOrder.shopping_order_id == shopping_order_id).first()
            if shopping_order is None:
                raise ShoppingOrderNotFoundException(f"Product with provided id: {shopping_order_id} not found.", 400)
            if name is not None:
                shopping_order.name = name
            if description is not None:
                shopping_order.description = description
            if price is not None:
                shopping_order.price = price
            if for_car_brand is not None:
                shopping_order.for_car_brand = for_car_brand
            if quantity_in_stock is not None:
                shopping_order.quantity_in_stock = quantity_in_stock
            self.db.add(shopping_order)
            self.db.commit()
            self.db.refresh(shopping_order)
            return shopping_order
        except Exception as e:
            raise e
