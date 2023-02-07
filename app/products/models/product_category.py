from uuid import uuid4
from sqlalchemy import Column, String
from app.db import Base


class ProductCategory(Base):
    __tablename__ = "product_category"
    product_category_id = Column(String(50), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)

    def __init__(self, name):
        self.name = name
