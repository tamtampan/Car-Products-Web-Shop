"""Cart Item Schemas"""

from pydantic import BaseModel
from pydantic.types import UUID4, PositiveInt

from app.products.schemas import ProductSchema


class CartItemSchema(BaseModel):
    """Cart Item Schema"""

    cart_item_id: UUID4
    quantity: PositiveInt
    shopping_cart_id: str
    # shopping_cart: ShoppingCartSchema
    product_id: str
    product: ProductSchema

    class Config:
        """Config"""

        orm_mode = True


class CartItemSchemaIn(BaseModel):
    """Cart Item Schema In"""

    quantity: PositiveInt
    shopping_cart_id: str
    product_id: str

    class Config:
        """Config"""

        orm_mode = True


class CartItemSchemaInCustomer(BaseModel):
    """Cart Item Schema In Customer"""

    quantity: PositiveInt
    customer_id: str
    product_id: str

    class Config:
        """Config"""

        orm_mode = True


class CartItemSchemaUpdate(BaseModel):
    """Cart Item Schema Update"""

    cart_item_id: str
    quantity: PositiveInt

    class Config:
        """Config"""

        orm_mode = True
