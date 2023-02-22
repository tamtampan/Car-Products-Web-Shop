"""Office Controller Module"""

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.offices.exceptions import OfficeNotFoundError
from app.offices.services import OfficeService


class OfficeController:
    """Office Controller"""

    @staticmethod
    def create(
        name: str, phone: str, address: str, city: str, country: str, postal_code: str, territory: str
    ) -> object:
        """Crate Office"""

        try:
            office = OfficeService.create(name, phone, address, city, country, postal_code, territory)
            return office
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Office with provided name already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(office_id: str) -> object:
        """Read by id"""

        try:
            office = OfficeService.read_by_id(office_id)
            return office
        except OfficeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all() -> list[object]:
        """Read all"""

        try:
            offices = OfficeService.read_all()
            return offices
        except OfficeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No offices in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(office_id: str) -> Response:
        """Delete by id"""

        try:
            OfficeService.delete_by_id(office_id)
            return Response(content=f"Office with id - {office_id} is deleted.")
        except OfficeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(
                status_code=400,
                detail="First you have to delete all employees and shopping orders " "from this office.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

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
            office = OfficeService.update(office_id, name, phone, address, city, country, postal_code, territory)
            return office
        except OfficeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_name(name: str) -> object:
        """It reads an office by name."""

        try:
            office = OfficeService.read_by_name(name)
            return office
        except OfficeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
