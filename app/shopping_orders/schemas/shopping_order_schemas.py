from datetime import date
from pydantic import BaseModel
from pydantic.types import UUID4, PositiveFloat
from app.users.schemas import CustomerSchema
from app.offices.schemas import OfficeSchema


class ShoppingOrderSchema(BaseModel):
    shopping_order_id: UUID4
    total_price: PositiveFloat
    status: int
    order_date: date
    shipped_date: date

    customer_id: str
    customer: CustomerSchema
    office_id: str
    office: OfficeSchema

    class Config:
        orm_mode = True


class ShoppingOrderSchemaIn(BaseModel):
    total_price: PositiveFloat
    status: int
    order_date: date
    shipped_date: date

    customer_id: str
    office_id: str

    class Config:
        orm_mode = True
