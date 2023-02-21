from pydantic import ValidationError
from app.carts.services import CartItemService, ShoppingCartService
from app.products.services import ProductService
from fastapi import HTTPException, Response
from app.carts.exceptions import CartItemNotFoundError, ShoppingCartNotFoundError, QuantityNotValid
from app.products.exceptions import ProductNotFoundError
from app.users.exceptions import CustomerNotFoundError


class CartItemController:
    """This class is responsible for managing the cart items"""
    @staticmethod
    def create_by_customer_id(quantity: int, customer_id: str, product_id: str) -> object:
        try:
            shopping_cart = ShoppingCartService.read_by_customer_id(customer_id)
            product = ProductService.read_by_id(product_id)
            cart_item = CartItemService.create(quantity, shopping_cart.shopping_cart_id, product_id)
            amount = quantity * product.price
            ShoppingCartService.update(shopping_cart.shopping_cart_id, amount)
            return cart_item
        except CustomerNotFoundError as e:
            raise HTTPException(status_code=400, detail=e.message)
        except ShoppingCartNotFoundError:
            raise HTTPException(status_code=400, detail=f"You can't create cart item with no existing shopping cart.")
        except ProductNotFoundError:
            raise HTTPException(status_code=400, detail=f"You can't create cart item with no existing product.")
        except QuantityNotValid as e:
            raise HTTPException(status_code=400, detail=e.message)
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create(quantity: int, shopping_cart_id: str, product_id: str) -> object:
        """It creates a cart item with the given quantity, shopping cart id and product id

        Parameters
        ----------
        quantity : int
            int - The quantity of the product in the cart item.
        shopping_cart_id : str
            The id of the shopping cart that the cart item belongs to.
        product_id : str
            The id of the product that is being added to the cart.

        Returns
        -------
            The cart item object.

        """

        try:
            ShoppingCartService.read_by_id(shopping_cart_id)
            product = ProductService.read_by_id(product_id)
            cart_item = CartItemService.create(quantity, shopping_cart_id, product_id)
            amount = quantity * product.price
            ShoppingCartService.update(shopping_cart_id, amount)
            return cart_item
        except ShoppingCartNotFoundError:
            raise HTTPException(status_code=400, detail=f"You can't create cart item with no existing shopping cart.")
        except ProductNotFoundError:
            raise HTTPException(status_code=400, detail=f"You can't create cart item with no existing product.")
        except QuantityNotValid as e:
            raise HTTPException(status_code=400, detail=e.message)
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(cart_item_id: str) -> object:
        try:
            cart_item = CartItemService.read_by_id(cart_item_id)
            return cart_item
        except CartItemNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all() -> list[object]:
        try:
            cart_items = CartItemService.read_all()
            return cart_items
        except CartItemNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No cart items in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_shopping_cart_id(shopping_cart_id: str) -> list[object]:
        try:
            ShoppingCartService.read_by_id(shopping_cart_id)
            cart_items = CartItemService.read_by_shopping_cart_id(shopping_cart_id)
            return cart_items
        except ShoppingCartNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except CartItemNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No cart items in this shopping cart.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(cart_item_id: str) -> Response:
        try:
            cart_item = CartItemService.read_by_id(cart_item_id)
            product = ProductService.read_by_id(cart_item.product_id)
            amount = cart_item.quantity * product.price
            ShoppingCartService.update(cart_item.shopping_cart_id, amount, True)

            CartItemService.delete_by_id(cart_item_id)
            return Response(status_code=200, content=f"Cart item with id - {cart_item_id} deleted.")
        except CartItemNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_quantity(cart_item_id: str, quantity: int) -> object:
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

        except CartItemNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except QuantityNotValid as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
