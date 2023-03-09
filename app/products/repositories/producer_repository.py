"""Producer Repository"""
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.products.models import Producer, Product


class ProducerRepository:
    """Producer Repository"""

    def __init__(self, db: Session):
        self.db = db

    def create(self, name, address, description) -> Producer:
        """Create"""

        try:
            producer = Producer(name, address, description)
            self.db.add(producer)
            self.db.commit()
            self.db.refresh(producer)
            return producer
        except Exception as exc:
            raise exc

    def read_by_id(self, producer_id: str) -> object:
        """Read by id"""

        try:
            producer = self.db.query(Producer).filter(Producer.producer_id == producer_id).first()
            return producer
        except Exception as exc:
            raise exc

    def read_by_name(self, name: str) -> object:
        """Read by name"""

        try:
            producer = self.db.query(Producer).filter(Producer.name == name).first()
            return producer
        except Exception as exc:
            raise exc

    def read_all(self) -> list[object]:
        """Read all"""

        try:
            producers = self.db.query(Producer).all()
            return producers
        except Exception as exc:
            raise exc

    def delete_by_id(self, producer_id: str) -> bool or None:
        """Delete by id"""

        try:
            producer = self.db.query(Producer).filter(Producer.producer_id == producer_id).first()
            if producer is None:
                return None
            self.db.delete(producer)
            self.db.commit()
            return True
        except Exception as exc:
            raise exc

    def update(self, producer_id: str, name: str = None, address: str = None, description: str = None) -> object:
        """Update"""

        try:
            producer = self.db.query(Producer).filter(Producer.producer_id == producer_id).first()
            if producer is None:
                return None
            if name is not None:
                producer.name = name
            if address is not None:
                producer.address = address
            if description is not None:
                producer.description = description
            self.db.add(producer)
            self.db.commit()
            self.db.refresh(producer)
            return producer
        except Exception as exc:
            raise exc

    # def read_producers_by_descending_number_of_products(self) -> list[object]:
    #     try:
    #         producers = []
    #         result = (
    #             self.db.query(Producer, func.count(Product.product_id))
    #             .join(Producer)
    #             .group_by(Product.producer_id)
    #         )
    #         # ovo u servis!
    #         for row in result:
    #             producer = row[0]
    #             producer.number_products = row[1]
    #             producers.append(producer)
    #         return producers
    #     except Exception as exc:
    #         raise exc
