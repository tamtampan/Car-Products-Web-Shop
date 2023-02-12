from pydantic import BaseModel
from pydantic import UUID4
from app.products.schemas import ProducerSchema, ProductCategorySchema


class ProductSchema(BaseModel):
    product_id: UUID4
    name: str
    description: str
    code: str
    price: float
    for_car_brand: str
    quantity_in_stock: int
    producer_id: str
    producer: ProducerSchema
    product_category_id: str
    product_category: ProductCategorySchema

    class Config:
        orm_mode = True


class ProductSchemaIn(BaseModel):
    name: str
    description: str
    code: str
    price: float
    for_car_brand: str
    quantity_in_stock: int
    producer_id: str
    product_category_id: str

    class Config:
        orm_mode = True
