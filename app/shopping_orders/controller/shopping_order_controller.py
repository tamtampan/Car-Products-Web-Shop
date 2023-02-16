from app.users.services import CustomerService
from app.offices.services import OfficeService
from app.shopping_orders.services import ShoppingOrderService
from fastapi import HTTPException, Response
from app.users.exceptions import CustomerNotFoundException
from app.offices.exceptions import OfficeNotFoundException
from app.shopping_orders.exceptions import ShoppingOrderNotFoundException


class ShoppingOrderController:

    @staticmethod
    def create(total_price: float, status: int, order_date: str, shipped_date: str, customer_id: str,
               office_id: str):
        try:
            CustomerService.read_by_id(customer_id)
            OfficeService.read_by_id(office_id)
            shopping_order = ShoppingOrderService.create(total_price, status, order_date, shipped_date, customer_id,
                                                         office_id)
            return shopping_order
        except CustomerNotFoundException as e:
            raise HTTPException(status_code=400, detail=e.message)
        except OfficeNotFoundException as e:
            raise HTTPException(status_code=400, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(shopping_order_id: str):
        try:
            shopping_order = ShoppingOrderService.read_by_id(shopping_order_id)
            return shopping_order
        except ShoppingOrderNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all():
        try:
            shopping_order = ShoppingOrderService.read_all()
            return shopping_order
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(shopping_order_id: str):
        try:
            ShoppingOrderService.delete_by_id(shopping_order_id)
            return Response(status_code=200, content=f"Shopping order with id - {shopping_order_id} deleted.")
        except ShoppingOrderNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(shopping_order_id: str, status: int = None, shipped_date: str = None):
        try:
            shopping_order = ShoppingOrderService.update(shopping_order_id, status, shipped_date)
            return shopping_order
        except ShoppingOrderNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
