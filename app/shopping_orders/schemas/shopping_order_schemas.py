from datetime import date
from pydantic import BaseModel
from pydantic.types import UUID4
from app.users.schemas import CustomerSchema
from app.offices.schemas import OfficeSchema
from typing import Optional, List


class ShoppingOrderSchema(BaseModel):
    shopping_order_id: UUID4
    total_price: float
    shipping_cost: float
    status: int
    order_date: date
    shipped_date: Optional[date]

    customer_id: str
    customer: CustomerSchema
    office_id: str
    office: OfficeSchema

    class Config:
        orm_mode = True


class ShoppingOrderSchemaIn(BaseModel):
    total_price: float
    shipping_cost: float
    status: int
    order_date: str
    shipped_date: Optional[str]

    customer_id: str
    office_id: str

    class Config:
        orm_mode = True


class ShoppingOrderSchemaOut(BaseModel):
    shopping_order_id: UUID4
    total_price: float
    shipping_cost: float
    status: int
    order_date: date
    shipped_date: Optional[date]

    customer_id: str
    customer: CustomerSchema
    office_id: str
    office: OfficeSchema
    items: List[object]

    class Config:
        orm_mode = True
