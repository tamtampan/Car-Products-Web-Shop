from datetime import date
from typing import List, Optional

from pydantic import BaseModel
from pydantic.types import UUID4

from app.offices.schemas import OfficeSchema
from app.users.schemas import CustomerSchema


class ShoppingOrderSchema(BaseModel):
    """Shopping Order Schema"""

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
    """Shopping Order Schema In"""

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
    """Shopping Order Schema Out"""

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


class ShoppingOrderMakeSchema(BaseModel):
    """Shopping Order Make Schema"""

    customer_id: str
    office_id: str

    class Config:
        orm_mode = True


class ShoppingOrderSchemaUpdateStatus(BaseModel):
    """Shopping Order Schema Update Status"""

    shopping_order_id: str
    shipping_cost: Optional[float]
    status: Optional[int]
    shipped_date: Optional[str]

    class Config:
        orm_mode = True


class ShoppingOrderSchemaUpdateTotalPrice(BaseModel):
    """Shopping Order Schema Update Total Price"""

    shopping_order_id: str
    amount: float
    subtract: Optional[bool]

    class Config:
        orm_mode = True
