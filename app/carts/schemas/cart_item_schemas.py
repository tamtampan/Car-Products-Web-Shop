from pydantic import BaseModel
from pydantic import UUID4
from .shopping_cart_schemas import ShoppingCartSchema
from app.products.schemas import ProductSchema


class CartItemSchema(BaseModel):
    cart_item_id: UUID4
    quantity: int
    shopping_cart_id: str
    shopping_cart: ShoppingCartSchema
    product_id: str
    product: ProductSchema

    class Config:
        orm_mode = True


class CartItemSchemaIn(BaseModel):
    quantity: int
    shopping_cart_id: str
    product_id: str

    class Config:
        orm_mode = True
