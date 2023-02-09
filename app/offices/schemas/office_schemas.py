from pydantic import BaseModel
from pydantic import UUID4


class OfficeSchema(BaseModel):
    office_id: UUID4
    name: str
    phone: str
    address: str
    city: str
    country: str
    postal_code: str
    territory: str

    class Config:
        orm_mode = True


class OfficeSchemaIn(BaseModel):
    name: str
    phone: str
    address: str
    city: str
    country: str
    postal_code: str
    territory: str

    class Config:
        orm_mode = True
