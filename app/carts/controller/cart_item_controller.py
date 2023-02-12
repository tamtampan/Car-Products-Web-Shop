from app.carts.services import CartItemService, ShoppingCartService
from app.products.services import ProductService
from fastapi import HTTPException, Response
from app.carts.exceptions import CartItemNotFoundException, ShoppingCartNotFoundException
from app.products.exceptions import ProductNotFoundException


class CartItemController:

    @staticmethod
    def create(quantity: int, shopping_cart_id: str, product_id: str):
        try:
            ShoppingCartService.read_by_id(shopping_cart_id)
            ProductService.read_by_id(product_id)
            cart_item = CartItemService.create(quantity, shopping_cart_id, product_id)
            return cart_item
        except ShoppingCartNotFoundException:
            raise HTTPException(status_code=400, detail=f"You can't create cart item with no existing shopping cart.")
        except ProductNotFoundException:
            raise HTTPException(status_code=400, detail=f"You can't create cart item with no existing product.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_by_id(cart_item_id: str):
        try:
            cart_item = CartItemService.read_by_id(cart_item_id)
            return cart_item
        except CartItemNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all():
        try:
            cart_item = CartItemService.read_all()
            return cart_item
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(cart_item_id: str):
        try:
            CartItemService.delete_by_id(cart_item_id)
            return Response(status_code=200, content=f"Cart item with id - {cart_item_id} deleted.")
        except CartItemNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_quantity(cart_item_id: str, quantity: int):
        try:
            cart_item = CartItemService.update_quantity(cart_item_id, quantity)
            return cart_item
        except CartItemNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
