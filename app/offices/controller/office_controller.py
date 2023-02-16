from sqlalchemy.exc import IntegrityError
from app.offices.services import OfficeService
from fastapi import HTTPException, Response
from app.offices.exceptions import *


class OfficeController:

    @staticmethod
    def create(name, phone, address, city, country, postal_code, territory):
        try:
            office = OfficeService.create(name, phone, address, city, country, postal_code, territory)
            return office
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Office with that name already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(office_id: str):
        try:
            office = OfficeService.read_by_id(office_id)
            return office
        except OfficeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all():
        office = OfficeService.read_all()
        return office

    @staticmethod
    def delete_by_id(office_id: str):
        try:
            OfficeService.delete_by_id(office_id)
            return Response(content=f"Office with id - {office_id} is deleted")
        except OfficeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(office_id: str, name: str = None, phone: str = None, address: str = None, city: str = None,
               country: str = None, postal_code: str = None, territory: str = None):
        try:
            office = OfficeService.update(office_id, name, phone, address, city, country, postal_code, territory)
            return office
        except OfficeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
