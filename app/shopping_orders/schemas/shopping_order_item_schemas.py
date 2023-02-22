from pydantic import BaseModel
from pydantic.types import UUID4, PositiveInt


class ShoppingOrderItemSchema(BaseModel):
    """Shopping Order Item Schema"""

    shopping_order_item_id: UUID4
    quantity: PositiveInt

    product_id: str
    shopping_order_id: str

    class Config:
        orm_mode = True


class ShoppingOrderItemSchemaIn(BaseModel):
    """Shopping Order Item Schema In"""

    quantity: PositiveInt

    product_id: str
    shopping_order_id: str

    class Config:
        orm_mode = True
