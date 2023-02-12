from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Customer(Base):
    __tablename__ = "customer"
    customer_id = Column(String(50), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    postal_code = Column(String(50), nullable=False)

    user_id = Column(String(50), ForeignKey("user.user_id"), nullable=False, unique=True)
    user = relationship("User", lazy='subquery')

    def __init__(self, name, surname, phone, address, city, country, postal_code, user_id):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.address = address
        self.city = city
        self.country = country
        self.postal_code = postal_code
        self.user_id = user_id
