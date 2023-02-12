from sqlalchemy.exc import IntegrityError
from app.carts.services import ShoppingCartService
from app.users.services import CustomerService
from fastapi import HTTPException, Response
from app.users.exceptions import CustomerNotFoundException
from app.carts.exceptions import ShoppingCartNotFoundException, ShoppingCartTotalCostError


class ShoppingCartController:

    @staticmethod
    def create(customer_id):
        try:
            CustomerService.read_by_id(customer_id)
            shopping_cart = ShoppingCartService.create(customer_id)
            return shopping_cart
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"This customer account already has shopping cart.")
        except CustomerNotFoundException:
            raise HTTPException(status_code=400, detail=f"You can not create shopping cart if you are not customer.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_by_id(shopping_cart_id: str):
        try:
            shopping_cart = ShoppingCartService.read_by_id(shopping_cart_id)
            return shopping_cart
        except ShoppingCartNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all():
        try:
            shopping_cart = ShoppingCartService.read_all()
            return shopping_cart
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(shopping_cart_id: str):
        try:
            ShoppingCartService.delete_by_id(shopping_cart_id)
            return Response(status_code=200, content=f"Shopping cart with id - {shopping_cart_id} deleted.")
        except ShoppingCartNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(shopping_cart_id: str, amount: float, subtract: bool = False):
        try:
            shopping_cart = ShoppingCartService.update(shopping_cart_id, amount, subtract)
            return shopping_cart
        except ShoppingCartNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ShoppingCartTotalCostError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
