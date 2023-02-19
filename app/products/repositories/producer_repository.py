from sqlalchemy.orm import Session
from app.products.models import Producer


class ProducerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name, address, description) -> object:
        try:
            producer = Producer(name, address, description)
            self.db.add(producer)
            self.db.commit()
            self.db.refresh(producer)
            return producer
        except Exception as e:
            raise e

    def read_by_id(self, producer_id: str) -> object:
        try:
            producer = self.db.query(Producer).filter(Producer.producer_id == producer_id).first()
            return producer
        except Exception as e:
            raise e

    def read_by_name(self, name: str) -> object:
        try:
            producer = self.db.query(Producer).filter(Producer.name == name).first()
            return producer
        except Exception as e:
            raise e

    def read_all(self) -> list[object]:
        try:
            producers = self.db.query(Producer).all()
            return producers
        except Exception as e:
            raise e

    def delete_by_id(self, producer_id: str) -> bool or None:
        try:
            producer = self.db.query(Producer).filter(Producer.producer_id == producer_id).first()
            if producer is None:
                return None
            self.db.delete(producer)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self, producer_id: str, name: str = None, address: str = None, description: str = None) -> object:
        try:
            producer = self.db.query(Producer).filter(Producer.producer_id == producer_id).first()
            if producer is None:
                return None
            if name is not None:
                producer.name = name
            if address is not None:
                producer.address = address
            if description is not None:
                producer.city = description
            self.db.add(producer)
            self.db.commit()
            self.db.refresh(producer)
            return producer
        except Exception as e:
            raise e
