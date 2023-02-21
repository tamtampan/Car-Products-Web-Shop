from sqlalchemy.exc import IntegrityError
from app.offices.services import OfficeService
from fastapi import HTTPException, Response
from app.offices.exceptions import *


class OfficeController:

    @staticmethod
    def create(name: str, phone: str, address: str, city: str, country: str, postal_code: str,
               territory: str) -> object:
        try:
            office = OfficeService.create(name, phone, address, city, country, postal_code, territory)
            return office
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Office with provided name already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(office_id: str) -> object:
        try:
            office = OfficeService.read_by_id(office_id)
            return office
        except OfficeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all() -> list[object]:
        try:
            offices = OfficeService.read_all()
            return offices
        except OfficeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No offices in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(office_id: str) -> Response:
        try:
            OfficeService.delete_by_id(office_id)
            return Response(content=f"Office with id - {office_id} is deleted.")
        except OfficeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="First you have to delete all employees and shopping orders "
                                                        "from this office.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(office_id: str, name: str = None, phone: str = None, address: str = None, city: str = None,
               country: str = None, postal_code: str = None, territory: str = None) -> object:
        try:
            office = OfficeService.update(office_id, name, phone, address, city, country, postal_code, territory)
            return office
        except OfficeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_name(name: str) -> object:
        try:
            office = OfficeService.read_by_name(name)
            return office
        except OfficeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
