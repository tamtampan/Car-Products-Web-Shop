from app.offices.repositories.office_repository import OfficeRepository
from app.db.database import SessionLocal


class OfficeService:

    @staticmethod
    def create(name, phone, address, city, country, postal_code, territory):
        try:
            with SessionLocal() as db:
                office_repository = OfficeRepository(db)
                return office_repository.create(name, phone, address, city, country, postal_code, territory)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(office_id: str):
        try:
            with SessionLocal() as db:
                office_repository = OfficeRepository(db)
                return office_repository.read_by_id(office_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                office_repository = OfficeRepository(db)
                return office_repository.read_all()
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(office_id: str):
        try:
            with SessionLocal() as db:
                office_repository = OfficeRepository(db)
                office_repository.delete_by_id(office_id)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def update(office_id: str, name: str = None, phone: str = None, address: str = None, city: str = None,
               country: str = None, postal_code: str = None, territory: str = None):
        try:
            with SessionLocal() as db:
                office_repository = OfficeRepository(db)
                return office_repository.update(office_id, name, phone, address, city, country, postal_code, territory)
        except Exception as e:
            raise e
