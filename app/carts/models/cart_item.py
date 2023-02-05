from uuid import uuid4
from sqlalchemy import Column, String, Integer, ForeignKey
from app.db import Base


class CartItem(Base):
    __tablename__ = "cart_item"
    cart_item_id = Column(String(50), primary_key=True, default=uuid4)
    quantity = Column(Integer, default=1, nullable=False)

    shopping_cart_id = Column(String(50), ForeignKey("shopping_cart.shopping_cart_id"), nullable=False)

    def __init__(self, shopping_cart_id, quantity=1):
        self.shopping_cart_id = shopping_cart_id
        self.quantity = quantity
