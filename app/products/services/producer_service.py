from app.products.repositories.producer_repository import ProducerRepository
from app.db.database import SessionLocal


class ProducerService:

    @staticmethod
    def create(name: str, address: str, description: str):
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                return producer_repository.create(name, address, description)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(producer_id: str):
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                return producer_repository.read_by_id(producer_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_name(name: str):
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                return producer_repository.read_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                return producer_repository.read_all()
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(producer_id: str):
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                return producer_repository.delete_by_id(producer_id)
        except Exception as e:
            raise e

    @staticmethod
    def update(producer_id: str, name: str = None, address: str = None, description: str = None):
        try:
            with SessionLocal() as db:
                producer_repository = ProducerRepository(db)
                return producer_repository.update(producer_id, name, address, description)
        except Exception as e:
            raise e
