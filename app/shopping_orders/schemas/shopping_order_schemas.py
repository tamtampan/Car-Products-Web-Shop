from datetime import date
from pydantic import BaseModel
from pydantic import UUID4
from app.users.schemas import CustomerSchema
from app.offices.schemas import OfficeSchema


class ShoppingOrderSchema(BaseModel):
    shopping_order_id: UUID4
    total_price: float
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
    total_price: float
    status: int
    order_date: date
    shipped_date: date

    customer_id: str
    office_id: str

    class Config:
        orm_mode = True
