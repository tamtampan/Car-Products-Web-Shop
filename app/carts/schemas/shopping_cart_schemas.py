from pydantic import BaseModel, UUID4


class ShoppingCartSchema(BaseModel):
    shopping_cart_id: UUID4
    total_cost: float
    customer_id: str
    # customer: CustomerSchema

    class Config:
        orm_mode = True


class ShoppingCartSchemaIn(BaseModel):
    customer_id: str

    class Config:
        orm_mode = True
