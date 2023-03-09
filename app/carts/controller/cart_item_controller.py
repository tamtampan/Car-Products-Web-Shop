"""Cart Item Controller Module"""

from fastapi import HTTPException, Response
from pydantic import ValidationError
from starlette.responses import JSONResponse

from app.carts.exceptions import CartItemNotFoundError, QuantityNotValid, ShoppingCartNotFoundError
from app.carts.services import CartItemService, ShoppingCartService
from app.products.exceptions import ProductNotFoundError
from app.products.services import ProductService
from app.users.exceptions import CustomerNotFoundError


class CartItemController:
    """Cart Item Controller"""

    @staticmethod
    def create_by_customer_id(quantity: int, customer_id: str, product_id: str) -> object:
        """
        It creates a cart item by customer id, quantity, product id
        :param quantity: int
        :type quantity: int
        :param customer_id: The id of the customer who owns the shopping cart
        :type customer_id: str
        :param product_id: The id of the product that the customer wants to add to the shopping cart
        :type product_id: str
        :return: The cart item object is being returned.
        """

        try:
            shopping_cart = ShoppingCartService.read_by_customer_id(customer_id)
            product = ProductService.read_by_id(product_id)
            cart_item = CartItemService.create(quantity, shopping_cart.shopping_cart_id, product_id)
            amount = quantity * product.price
            ShoppingCartService.update(shopping_cart.shopping_cart_id, amount)
            return cart_item
        except CustomerNotFoundError as exc:
            raise HTTPException(status_code=404, detail=exc.message)
        except ShoppingCartNotFoundError:
            raise HTTPException(status_code=404, detail="You can't create cart item with no existing shopping cart.")
        except ProductNotFoundError:
            raise HTTPException(status_code=404, detail="You can't create cart item with no existing product.")
        except QuantityNotValid as exc:
            raise HTTPException(status_code=400, detail=exc.message)
        except ValidationError as exc:
            raise HTTPException(status_code=400, detail=str(exc))
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def create(quantity: int, shopping_cart_id: str, product_id: str) -> object:
        """
        It creates a cart item, updates the shopping cart's amount and returns the cart item
        :param quantity: int
        :type quantity: int
        :param shopping_cart_id: The id of the shopping cart that the cart item belongs to
        :type shopping_cart_id: str
        :param product_id: The id of the product to be added to the cart
        :type product_id: str
        :return: The cart item object is being returned.
        """

        try:
            ShoppingCartService.read_by_id(shopping_cart_id)
            product = ProductService.read_by_id(product_id)
            cart_item = CartItemService.create(quantity, shopping_cart_id, product_id)
            amount = quantity * product.price
            ShoppingCartService.update(shopping_cart_id, amount)
            return cart_item
        except ShoppingCartNotFoundError:
            raise HTTPException(status_code=404, detail="You can't create cart item with no existing shopping cart.")
        except ProductNotFoundError:
            raise HTTPException(status_code=404, detail="You can't create cart item with no existing product.")
        except QuantityNotValid as exc:
            raise HTTPException(status_code=400, detail=exc.message)
        except ValidationError as exc:
            raise HTTPException(status_code=400, detail=str(exc))
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_by_id(cart_item_id: str) -> object:
        """Read by id"""

        try:
            cart_item = CartItemService.read_by_id(cart_item_id)
            return cart_item
        except CartItemNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_all() -> list[object]:
        """Read all"""

        try:
            cart_items = CartItemService.read_all()
            return cart_items
        except CartItemNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="No cart items in system.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_by_shopping_cart_id(shopping_cart_id: str) -> list[object]:
        """Read by cart id"""

        try:
            ShoppingCartService.read_by_id(shopping_cart_id)
            cart_items = CartItemService.read_by_shopping_cart_id(shopping_cart_id)
            return cart_items
        except ShoppingCartNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except CartItemNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="No cart items in this shopping cart.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def delete_by_id(cart_item_id: str) -> Response:
        """Delete by id"""
        try:
            cart_item = CartItemService.read_by_id(cart_item_id)
            product = ProductService.read_by_id(cart_item.product_id)
            amount = cart_item.quantity * product.price
            ShoppingCartService.update(cart_item.shopping_cart_id, amount, True)

            CartItemService.delete_by_id(cart_item_id)
            return JSONResponse(status_code=200, content=f"Cart item with id - {cart_item_id} deleted.")
        except CartItemNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def update_quantity(cart_item_id: str, quantity: int) -> object:
        """It updates the quantity of a cart item and updates the shopping cart total cost."""

        try:
            old_item = CartItemService.read_by_id(cart_item_id)
            product = ProductService.read_by_id(old_item.product_id)
            old_amount = product.price * old_item.quantity

            cart_item = CartItemService.update_quantity(cart_item_id, quantity)
            new_amount = product.price * quantity
            if old_amount != new_amount:
                flag = False
                if old_amount > new_amount:
                    flag = True
                amount = abs(old_amount - new_amount)
                ShoppingCartService.update(old_item.shopping_cart_id, amount, flag)
            return cart_item

        except CartItemNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except QuantityNotValid as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
