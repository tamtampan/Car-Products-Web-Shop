from uuid import uuid4
from sqlalchemy import Column, String
from app.db import Base


class Producer(Base):
    __tablename__ = "producer"
    producer_id = Column(String(50), primary_key=True, default=uuid4)
    producer_name = Column(String(50), nullable=False)
    producer_address = Column(String(100), nullable=False)
    producer_description = Column(String(500), nullable=False)

    def __init__(self, producer_name, producer_address, producer_description):
        self.producer_name = producer_name
        self.producer_address = producer_address
        self.producer_description = producer_description
