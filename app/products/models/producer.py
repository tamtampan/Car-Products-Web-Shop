from uuid import uuid4
from sqlalchemy import Column, String
from app.db import Base


class Producer(Base):
    __tablename__ = "producer"
    producer_id = Column(String(100), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False, unique=True)
    address = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)

    def __init__(self, name, address, description):
        self.name = name
        self.address = address
        self.description = description
