from pydantic import BaseModel
from pydantic import UUID4


class ProductCategorySchema(BaseModel):
    product_category_id: UUID4
    name: str

    class Config:
        orm_mode = True


class ProductCategorySchemaIn(BaseModel):
    name: str

    class Config:
        orm_mode = True
