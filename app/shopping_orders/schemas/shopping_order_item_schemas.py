from pydantic import BaseModel
from pydantic.types import UUID4, PositiveInt
from app.products.schemas import ProductSchema
from app.shopping_orders.schemas import ShoppingOrderSchema


class ShoppingOrderItemSchema(BaseModel):
    shopping_order_item_id: UUID4
    quantity: PositiveInt

    product_id: str
    # product: ProductSchema
    shopping_order_id: str
    # shopping_order: ShoppingOrderSchema

    class Config:
        orm_mode = True


class ShoppingOrderItemSchemaIn(BaseModel):
    quantity: PositiveInt

    product_id: str
    shopping_order_id: str

    class Config:
        orm_mode = True
