from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.products.models import Producer
from app.products.exceptions import ProducerNotFoundException


class ProducerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name, address, description):
        try:
            producer = Producer(name, address, description)
            self.db.add(producer)
            self.db.commit()
            self.db.refresh(producer)
            return producer
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_by_id(self, producer_id: str):
        producer = self.db.query(Producer).filter(Producer.producer_id == producer_id).first()
        if producer is None:
            raise ProducerNotFoundException(f"Producer with provided ID: {producer_id} not found.", 400)
        return producer

    def read_by_name(self, name: str):
        producer = self.db.query(Producer).filter(Producer.name == name).first()
        if producer is None:
            raise ProducerNotFoundException(f"Producer with provided name: {name} not found.", 400)
        return producer

    def read_all(self):
        producers = self.db.query(Producer).all()
        return producers

    def delete_by_id(self, producer_id: str):
        try:
            producer = self.db.query(Producer).filter(Producer.producer_id == producer_id).first()
            if producer is None:
                raise ProducerNotFoundException(f"Producer with provided ID: {producer_id} not found.", 400)
            self.db.delete(producer)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self, producer_id: str, name: str = None, address: str = None, description: str = None):
        try:
            producer = self.db.query(Producer).filter(Producer.producer_id == producer_id).first()
            if producer is None:
                raise ProducerNotFoundException(f"Producer with provided ID: {producer_id} not found.", 400)
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
