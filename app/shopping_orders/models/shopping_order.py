from uuid import uuid4
from sqlalchemy import Column, String, Float, Integer, Date, ForeignKey
from app.db import Base


class ShoppingOrder(Base):
    __tablename__ = "shopping_order"
    shopping_order_id = Column(String(100), primary_key=True, default=uuid4)
    total_price = Column(Float, nullable=False)
    status = Column(Integer, default=0)  # status 0 oznacava da su proizvodi poruceni i da je proces u inicijalnoj fazi
    # (faza pakovanja), status 1 bi oznacavao da je posiljka poslata a na primer status 2 da je isporucena
    order_date = Column(Date, nullable=False)
    shipped_date = Column(Date, default=None)

    customer_id = Column(String(100), ForeignKey("customer.customer_id"), nullable=False)
    office_id = Column(String(100), ForeignKey("office.office_id"), nullable=False)

    def __init__(self, total_price, order_date, shipped_date, customer_id, office_id, status=0):
        self.total_price = total_price
        self.status = status
        self.order_date = order_date
        self.shipped_date = shipped_date
        self.customer_id = customer_id
        self.office_id = office_id
