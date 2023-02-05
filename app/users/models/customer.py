from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Customer(Base):
    __tablename__ = "customer"
    customer_id = Column(String(50), primary_key=True, default=uuid4)
    customer_name = Column(String(50), nullable=False)
    customer_surname = Column(String(50), nullable=False)
    customer_phone = Column(String(50), nullable=False)
    customer_address = Column(String(100), nullable=False)
    customer_city = Column(String(50), nullable=False)
    customer_state = Column(String(50), nullable=False)
    customer_postal_code = Column(String(50), nullable=False)

    user_id = Column(String(50), ForeignKey("user.user_id"), nullable=False)
    user = relationship("User", lazy='subquery')

    def __init__(self, customer_name, customer_surname, customer_phone, customer_address, customer_city,
                 customer_state, customer_postal_code, user_id):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.customer_phone = customer_phone
        self.customer_address = customer_address
        self.customer_city = customer_city
        self.customer_state = customer_state
        self.customer_postal_code = customer_postal_code
        self.user_id = user_id
