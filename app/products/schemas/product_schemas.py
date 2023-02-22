from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4, PositiveFloat


class ProductSchema(BaseModel):
    """Product Schema"""

    product_id: UUID4
    name: str
    description: str
    code: str
    price: PositiveFloat
    for_car_brand: Optional[str]
    quantity_in_stock: int
    producer_id: str
    product_category_id: str

    class Config:
        orm_mode = True


class ProductSchemaIn(BaseModel):
    """Product Schema In"""

    name: str
    description: str
    code: str
    price: PositiveFloat
    for_car_brand: str
    quantity_in_stock: int
    producer_id: str
    product_category_id: str

    class Config:
        orm_mode = True


class ProductSchemaUpdate(BaseModel):
    """Product Schema Update"""

    product_id: str
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    for_car_brand: Optional[str]
    quantity_in_stock: Optional[int]

    class Config:
        orm_mode = True


class ProductSchemaUpdateQuantity(BaseModel):
    """Product Schema Update Quantity"""

    product_id: str
    amount: int
    subtract: Optional[bool]

    class Config:
        orm_mode = True


class ProductSchemaCount(BaseModel):
    """Product Schema"""

    product_id: UUID4
    name: str
    description: str
    code: str
    price: PositiveFloat
    for_car_brand: Optional[str]
    quantity_in_stock: int
    producer_id: str
    product_category_id: str
    number_sold: int

    class Config:
        orm_mode = True
