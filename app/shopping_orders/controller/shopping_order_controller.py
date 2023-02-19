from datetime import date

from sqlalchemy.exc import IntegrityError

from app.users.services import CustomerService
from app.offices.services import OfficeService
from app.products.services import ProductService
from app.shopping_orders.services import ShoppingOrderService, ShoppingOrderItemService
from fastapi import HTTPException, Response
from app.users.exceptions import CustomerNotFoundError
from app.offices.exceptions import OfficeNotFoundError
from app.shopping_orders.exceptions import ShoppingOrderNotFoundError, ShoppingOrderTotalPriceSubtractionError


class ShoppingOrderController:
    """This class is responsible for handling all the requests related to shopping orders"""

    @staticmethod
    def create(total_price: float, shipping_cost: float, status: int, order_date: str, shipped_date: str,
               customer_id: str, office_id: str) -> object:
        """It creates a shopping order

        Parameters
        ----------
        total_price : float
        shipping_cost: float
        status : int
        order_date : str
        shipped_date: str
        shipped_date : str
        customer_id : str
        office_id : str

        Returns
        -------
            The created shopping order.
            """

        try:
            CustomerService.read_by_id(customer_id)
            OfficeService.read_by_id(office_id)
            shopping_order = ShoppingOrderService.create(total_price, shipping_cost, status, order_date, shipped_date,
                                                         customer_id, office_id)
            return shopping_order
        except CustomerNotFoundError as e:
            raise HTTPException(status_code=400, detail=e.message)
        except OfficeNotFoundError as e:
            raise HTTPException(status_code=400, detail=e.message)
        except ValueError:
            raise HTTPException(status_code=400, detail="Date not in right form (yyyy-mm-dd).")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(shopping_order_id: str) -> object:
        try:
            shopping_order = ShoppingOrderService.read_by_id(shopping_order_id)
            return shopping_order
        except ShoppingOrderNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all() -> list[object]:
        try:
            shopping_orders = ShoppingOrderService.read_all()
            return shopping_orders
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(shopping_order_id: str) -> Response:
        try:
            ShoppingOrderService.delete_by_id(shopping_order_id)
            return Response(status_code=200, content=f"Shopping order with id - {shopping_order_id} deleted.")
        except ShoppingOrderNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Can not delete shopping order that has items in it.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(shopping_order_id: str, shipping_cost: float = None, status: int = None,
               shipped_date: str = None) -> object:
        try:
            shopping_order = ShoppingOrderService.update(shopping_order_id, shipping_cost, status, shipped_date)
            return shopping_order
        except ShoppingOrderNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_shopping_order_with_items(shopping_order_id: str) -> object:
        try:
            shopping_order = ShoppingOrderService.read_by_id(shopping_order_id)
            shopping_order.items = ShoppingOrderItemService.read_items_by_shopping_order_id(shopping_order_id)
            return shopping_order
        except ShoppingOrderNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_today_shopping_orders() -> list[object]:
        try:
            shopping_orders = ShoppingOrderService.read_today_shopping_orders()
            return shopping_orders
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def sum_today_profit() -> Response:
        try:
            profit = ShoppingOrderService.sum_today_profit()
            return Response(status_code=200, content=f"Profit for today is {profit} dinars.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_sum_total_price(shopping_order_id: str) -> object:
        try:
            total_price = 0
            items = ShoppingOrderItemService.read_items_by_shopping_order_id(shopping_order_id)
            for item in items:
                product = ProductService.read_by_id(item.product_id)
                total_price += product.price * item.quantity
            return ShoppingOrderService.update_total_price(shopping_order_id, total_price)
        except ShoppingOrderNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_total_price_for_amount(shopping_order_id: str, amount: float, subtract: bool = False) -> object:
        try:
            shopping_order = ShoppingOrderService.update_total_price_for_amount(shopping_order_id, amount, subtract)
            return shopping_order
        except ShoppingOrderTotalPriceSubtractionError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ShoppingOrderNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
