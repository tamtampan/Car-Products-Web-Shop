from pydantic import UUID4, BaseModel


class ProductCategorySchema(BaseModel):
    """Product Category Schema"""

    product_category_id: UUID4
    name: str

    class Config:
        orm_mode = True


class ProductCategorySchemaIn(BaseModel):
    """Product Category Schema In"""

    name: str

    class Config:
        orm_mode = True


class ProductCategorySchemaUpdate(BaseModel):
    """Product Category Schema Update"""

    product_category_id: str
    name: str

    class Config:
        orm_mode = True
