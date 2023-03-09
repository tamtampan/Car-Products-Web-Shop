"""Shopping cart controller"""

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.carts.exceptions import ShoppingCartNotFoundError, ShoppingCartTotalCostError
from app.carts.services import ShoppingCartService
from app.users.exceptions import CustomerNotFoundError
from app.users.services import CustomerService
from starlette.responses import JSONResponse


class ShoppingCartController:
    """Shopping Cart Controller"""

    @staticmethod
    def create(customer_id) -> object:
        """
        It creates a shopping cart for a customer
        :param customer_id: The id of the customer who owns the shopping cart
        :return: Shopping cart object
        """

        try:
            CustomerService.read_by_id(customer_id)
            shopping_cart = ShoppingCartService.create(customer_id)
            return shopping_cart
        except IntegrityError:
            raise HTTPException(status_code=400, detail="This customer account already has shopping cart.")
        except CustomerNotFoundError:
            raise HTTPException(status_code=400, detail="You can not create shopping cart if you are not customer.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_by_id(shopping_cart_id: str) -> object:
        try:
            shopping_cart = ShoppingCartService.read_by_id(shopping_cart_id)
            return shopping_cart
        except ShoppingCartNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_by_customer_id(customer_id: str) -> object:
        """
        It reads a shopping cart by customer id
        :param customer_id: str
        :type customer_id: str
        :return: The shopping cart object is being returned.
        """
        try:
            CustomerService.read_by_id(customer_id)
            shopping_cart = ShoppingCartService.read_by_customer_id(customer_id)
            return shopping_cart
        except CustomerNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except ShoppingCartNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_all() -> list[object]:
        try:
            shopping_cart = ShoppingCartService.read_all()
            return shopping_cart
        except ShoppingCartNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="No shopping cards in system.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def delete_by_id(shopping_cart_id: str) -> Response:
        try:
            ShoppingCartService.delete_by_id(shopping_cart_id)
            return JSONResponse(status_code=200, content=f"Shopping cart with id - {shopping_cart_id} deleted.")
        except ShoppingCartNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Can not delete shopping cart that has cart items.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def update(shopping_cart_id: str, amount: float, subtract: bool = False) -> object:
        """
        It updates the shopping cart for specific amount. Depends on subtract attribute,
          amount can be added to total cost of shopping cart or subtracted
        :param shopping_cart_id: The id of the shopping cart to update
        :type shopping_cart_id: str
        :param amount: The amount to be added to the shopping cart
        :type amount: float
        :param subtract: bool = False, defaults to False
        :type subtract: bool (optional)
        :return: The shopping cart object
        """
        try:
            shopping_cart = ShoppingCartService.update(shopping_cart_id, amount, subtract)
            return shopping_cart
        except ShoppingCartNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except ShoppingCartTotalCostError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def update_set_total_cost(shopping_cart_id: str, total_cost: float) -> object:
        """
        It updates the total cost of a shopping cart.
        It is used for setting total cost to 0 when cart becomes empty
        :param shopping_cart_id: str
        :type shopping_cart_id: str
        :param total_cost: float
        :type total_cost: float
        :return: The updated shopping cart object.
        """
        try:
            shopping_cart = ShoppingCartService.update_set_total_cost(shopping_cart_id, total_cost)
            return shopping_cart
        except ShoppingCartNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
