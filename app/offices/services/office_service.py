"""Office Service Module"""

from sqlalchemy.exc import IntegrityError

from app.db.database import SessionLocal
from app.offices.exceptions import *
from app.offices.repositories.office_repository import OfficeRepository


class OfficeService:
    """Office Service Class"""

    @staticmethod
    def create(
        name: str, phone: str, address: str, city: str, country: str, postal_code: str, territory: str
    ) -> object:
        """Create Office"""

        try:
            with SessionLocal() as db:
                office_repository = OfficeRepository(db)
                return office_repository.create(name, phone, address, city, country, postal_code, territory)
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(office_id: str) -> object:
        """Read by id"""

        try:
            with SessionLocal() as db:
                office_repository = OfficeRepository(db)
                office = office_repository.read_by_id(office_id)
                if office is None:
                    raise OfficeNotFoundError()
                return office
        except Exception as e:
            raise e

    @staticmethod
    def read_all() -> list[object]:
        """Read all"""

        try:
            with SessionLocal() as db:
                office_repository = OfficeRepository(db)
                offices = office_repository.read_all()
                if len(offices) == 0:
                    raise OfficeNotFoundError()
                return offices
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(office_id: str) -> bool:
        """Delete by id"""

        try:
            with SessionLocal() as db:
                office_repository = OfficeRepository(db)
                office_deleted = office_repository.delete_by_id(office_id)
                if office_deleted is None:
                    raise OfficeNotFoundError()
                return office_deleted
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def update(
        office_id: str,
        name: str = None,
        phone: str = None,
        address: str = None,
        city: str = None,
        country: str = None,
        postal_code: str = None,
        territory: str = None,
    ) -> object:
        """Update"""

        try:
            with SessionLocal() as db:
                office_repository = OfficeRepository(db)
                office = office_repository.update(
                    office_id, name, phone, address, city, country, postal_code, territory
                )
                if office is None:
                    raise OfficeNotFoundError()
                return office
        except Exception as e:
            raise e

    @staticmethod
    def read_by_name(name: str) -> object:
        """Read by name"""

        try:
            with SessionLocal() as db:
                office_repository = OfficeRepository(db)
                office = office_repository.read_by_name(name)
                if office is None:
                    raise OfficeNotFoundError()
                return office
        except Exception as e:
            raise e
