from typing import Optional

from pydantic import UUID4, BaseModel


class ProducerSchema(BaseModel):
    """Producer Schema"""

    producer_id: UUID4
    name: str
    address: str
    description: str

    class Config:
        orm_mode = True


class ProducerSchemaIn(BaseModel):
    """Producer Schema In"""

    name: str
    address: str
    description: str

    class Config:
        orm_mode = True


class ProducerSchemaUpdate(BaseModel):
    """Producer Schema Update"""

    producer_id: str
    name: Optional[str]
    address: Optional[str]
    description: Optional[str]
