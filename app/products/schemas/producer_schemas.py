from pydantic import BaseModel
from pydantic import UUID4


class ProducerSchema(BaseModel):
    producer_id: UUID4
    name: str
    address: str
    description: str

    class Config:
        orm_mode = True


class ProducerSchemaIn(BaseModel):
    name: str
    address: str
    description: str

    class Config:
        orm_mode = True
