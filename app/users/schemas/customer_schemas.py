from pydantic import BaseModel
from pydantic import UUID4
from app.users.schemas import UserSchema


class CustomerSchema(BaseModel):
    customer_id: UUID4
    name: str
    surname: str
    phone: str
    address: str
    city: str
    country: str
    postal_code: str
    user_id: str
    user: UserSchema

    class Config:
        orm_mode = True


class CustomerSchemaIn(BaseModel):
    name: str
    surname: str
    phone: str
    address: str
    city: str
    country: str
    postal_code: str
    user_id: str
