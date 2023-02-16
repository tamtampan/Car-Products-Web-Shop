from uuid import uuid4
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Product(Base):
    __tablename__ = "product"
    product_id = Column(String(100), primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    code = Column(String(50), unique=True)
    price = Column(Float, nullable=False)
    for_car_brand = Column(String(100))
    quantity_in_stock = Column(Integer)

    producer_id = Column(String(100), ForeignKey("producer.producer_id"), nullable=False)
    producer = relationship("Producer", lazy='subquery')
    product_category_id = Column(String(100), ForeignKey("product_category.product_category_id"), nullable=False)
    product_category = relationship("ProductCategory", lazy='subquery')

    def __init__(self, name, description, code, price, for_car_brand,
                 quantity_in_stock, producer_id, product_category_id):
        self.name = name
        self.description = description
        self.code = code
        self.price = price
        self.for_car_brand = for_car_brand
        self.quantity_in_stock = quantity_in_stock
        self.producer_id = producer_id
        self.product_category_id = product_category_id
