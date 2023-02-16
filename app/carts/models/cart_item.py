from uuid import uuid4
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class CartItem(Base):
    __tablename__ = "cart_item"
    cart_item_id = Column(String(100), primary_key=True, default=uuid4)
    quantity = Column(Integer, default=1, nullable=False)

    shopping_cart_id = Column(String(100), ForeignKey("shopping_cart.shopping_cart_id"), nullable=False)
    shopping_cart = relationship("ShoppingCart", lazy='subquery')
    product_id = Column(String(100), ForeignKey("product.product_id"), nullable=False)
    product = relationship("Product", lazy='subquery')

    def __init__(self, shopping_cart_id, product_id, quantity=1):
        self.shopping_cart_id = shopping_cart_id
        self.product_id = product_id
        self.quantity = quantity
