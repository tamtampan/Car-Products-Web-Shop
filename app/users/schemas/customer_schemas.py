from typing import Optional

from pydantic import UUID4, BaseModel

from app.carts.schemas import ShoppingCartSchema
from app.users.schemas import UserSchema


class CustomerSchema(BaseModel):
    """Customer Schema"""

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
    """Customer Schema In"""

    name: str
    surname: str
    phone: str
    address: str
    city: str
    country: str
    postal_code: str
    user_id: str


class CustomerSchemaOut(BaseModel):
    """Customer Schema Out"""

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


class CustomerSchemaUpdate(BaseModel):
    """Customer Schema Update"""

    customer_id: str
    name: Optional[str]
    surname: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    city: Optional[str]
    country: Optional[str]
    postal_code: Optional[str]
