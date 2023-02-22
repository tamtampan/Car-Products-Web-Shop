"""Shopping Cart Schemas"""

from typing import Optional

from pydantic import UUID4, BaseModel


class ShoppingCartSchema(BaseModel):
    """Shopping Cart Schema"""

    shopping_cart_id: UUID4
    total_cost: float
    customer_id: str

    class Config:
        """Config"""

        orm_mode = True


class ShoppingCartSchemaIn(BaseModel):
    """Shopping Cart Schema In"""

    customer_id: str

    class Config:
        """Config"""

        orm_mode = True


class ShoppingCartSchemaUpdate(BaseModel):
    """Shopping Cart Schema Update"""

    shopping_cart_id: str
    amount: float
    subtract: Optional[bool]

    class Config:
        """Config"""

        orm_mode = True
