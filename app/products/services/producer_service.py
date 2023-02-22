from sqlalchemy.exc import IntegrityError

from app.db.database import SessionLocal
from app.products.exceptions import ProducerNotFoundError
from app.products.repositories.producer_repository import ProducerRepository


class ProducerService:
    """Producer Service"""

    @staticmethod
    def create(name: str, address: str, description: str) -> object:
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                return producer_repository.create(name, address, description)
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(producer_id: str) -> object:
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                producer = producer_repository.read_by_id(producer_id)
                if producer is None:
                    raise ProducerNotFoundError()
                return producer
        except Exception as e:
            raise e

    @staticmethod
    def read_by_name(name: str) -> object:
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                producer = producer_repository.read_by_name(name)
                if producer is None:
                    raise ProducerNotFoundError()
                return producer
        except Exception as e:
            raise e

    @staticmethod
    def read_all() -> list[object]:
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                producers = producer_repository.read_all()
                if len(producers) == 0:
                    raise ProducerNotFoundError()
                return producers
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(producer_id: str) -> bool:
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                producer = producer_repository.delete_by_id(producer_id)
                if producer is None:
                    raise ProducerNotFoundError()
                return producer
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def update(producer_id: str, name: str = None, address: str = None, description: str = None) -> object:
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                producer = producer_repository.update(
                    producer_id=producer_id, name=name, address=address, description=description
                )
                if producer is None:
                    raise ProducerNotFoundError()
                return producer
        except Exception as e:
            raise e
