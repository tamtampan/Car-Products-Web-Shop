from app.products.services import ProducerService
from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from app.products.exceptions import *


class ProducerController:

    @staticmethod
    def create(name: str, address: str, description: str) -> object:
        try:
            producer = ProducerService.create(name, address, description)
            return producer
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Producer with provided name - {name} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(producer_id: str) -> object:
        try:
            producer = ProducerService.read_by_id(producer_id)
            return producer
        except ProducerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_name(name: str) -> object:
        try:
            producer = ProducerService.read_by_name(name)
            return producer
        except ProducerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all() -> list[object]:
        try:
            producers = ProducerService.read_all()
            return producers
        except ProducerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No producers in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(producer_id: str) -> Response:
        try:
            ProducerService.delete_by_id(producer_id)
            return Response(content=f"Producer with id - {producer_id} is deleted")
        except ProducerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Can not delete producer that has products in system.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update(producer_id: str, name: str = None, address: str = None, description: str = None) -> object:
        try:
            producer = ProducerService.update(producer_id, name, address, description)
            return producer
        except ProducerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
