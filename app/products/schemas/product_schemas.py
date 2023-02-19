from pydantic import BaseModel
from pydantic.types import UUID4, PositiveFloat
from typing import Optional


class ProductSchema(BaseModel):
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
