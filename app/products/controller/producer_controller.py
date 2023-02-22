"""Producer Controller Module"""

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.products.exceptions import ProducerNotFoundError
from app.products.services import ProducerService


class ProducerController:
    """Producer Controller"""

    @staticmethod
    def create(name: str, address: str, description: str) -> object:
        """
        It creates a producer.

        :param name: str - the name of the producer
        :type name: str
        :param address: str - the address of the producer
        :type address: str
        :param description: str - The description of the producer
        :type description: str
        :return: The producer object is being returned.
        """
        try:
            producer = ProducerService.create(name, address, description)
            return producer
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Producer with provided name - {name} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(producer_id: str) -> object:
        """Read by id"""

        try:
            producer = ProducerService.read_by_id(producer_id)
            return producer
        except ProducerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_name(name: str) -> object:
        """Read by name"""

        try:
            producer = ProducerService.read_by_name(name)
            return producer
        except ProducerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all() -> list[object]:
        """Read all"""

        try:
            producers = ProducerService.read_all()
            return producers
        except ProducerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No producers in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(producer_id: str) -> Response:
        """Delete by id"""

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
        """Update"""

        try:
            producer = ProducerService.update(
                producer_id=producer_id, name=name, address=address, description=description
            )
            return producer
        except ProducerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
