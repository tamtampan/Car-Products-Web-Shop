from uuid import uuid4
from sqlalchemy import Column, String, Float, Integer, ForeignKey

from app.db import Base


class Product(Base):
    __tablename__ = "product"
    product_id = Column(String(50), primary_key=True, default=uuid4)
    product_name = Column(String(100), nullable=False)
    product_description = Column(String(500))
    product_code = Column(String(50), unique=True)
    product_price = Column(Float, nullable=False)
    for_car_brand_or_model = Column(String(100))
    quantity_in_stock = Column(Integer)

    producer_id = Column(String(50), ForeignKey("producer.producer_id"), nullable=False)
    product_category_id = Column(String(50), ForeignKey("product_category.product_category_id"), nullable=False)

    def __init__(self, product_name, product_description, product_code, product_price, for_car_brand_or_model,
                 quantity_in_stock, producer_id, product_category_id):
        self.product_name = product_name
        self.product_description = product_description
        self.product_code = product_code
        self.product_price = product_price
        self.for_car_brand_or_model = for_car_brand_or_model
        self.quantity_in_stock = quantity_in_stock
        self.producer_id = producer_id
        self.product_category_id = product_category_id
