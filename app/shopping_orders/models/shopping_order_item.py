from uuid import uuid4
from sqlalchemy import Column, String, Integer, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship


class ShoppingOrderItem(Base):
    __tablename__ = "shopping_order_item"
    shopping_order_item_id = Column(String(100), primary_key=True, default=uuid4)
    quantity = Column(Integer, nullable=False, default=1)

    product_id = Column(String(100), ForeignKey("product.product_id"), nullable=False)
    product = relationship("Product", lazy='subquery')
    shopping_order_id = Column(String(100), ForeignKey("shopping_order.shopping_order_id"), nullable=False)
    shopping_order = relationship("ShoppingOrder", lazy='subquery')

    def __init__(self, quantity: int, product_id: str, shopping_order_id: str):
        self.quantity = quantity
        self.product_id = product_id
        self.shopping_order_id = shopping_order_id
