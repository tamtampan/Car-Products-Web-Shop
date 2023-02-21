from pydantic import BaseModel
from pydantic import UUID4
from app.users.schemas import UserSchema
from app.carts.schemas import ShoppingCartSchema


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


class CustomerSchemaOut(BaseModel):
    customer_id: UUID4
    name: str
    surname: str
    phone: str
    address: str
    city: str
    country: str
    postal_code: str
    user_id: str
    cart: ShoppingCartSchema

    class Config:
        orm_mode = True
