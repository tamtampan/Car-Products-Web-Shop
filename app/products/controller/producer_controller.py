from app.products.services import ProducerService
from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.products.exceptions import *


class ProducerController:

    @staticmethod
    def create(name: str, address: str, description: str):
        try:
            producer = ProducerService.create(name, address, description)
            return producer
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Producer with provided name - {name} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(producer_id: str):
        try:
            producer = ProducerService.read_by_id(producer_id)
            return producer
        except ProducerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_name(name: str):
        try:
            producer = ProducerService.read_by_name(name)
            return producer
        except ProducerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all():
        try:
            producers = ProducerService.read_all()
            return producers
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(producer_id: str):
        try:
            ProducerService.delete_by_id(producer_id)
            return Response(content=f"Producer with id - {producer_id} is deleted")
        except ProducerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update(producer_id: str, name: str = None, address: str = None, description: str = None):
        try:
            producer = ProducerService.update(producer_id, name, address, description)
            return producer
        except ProducerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
