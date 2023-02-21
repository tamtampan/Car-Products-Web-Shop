from sqlalchemy.exc import IntegrityError

from app.products.exceptions import ProductOutOfStockError, ProductNotFoundError
from app.users.services import CustomerService
from app.offices.services import OfficeService
from app.products.services import ProductService
from app.shopping_orders.services import ShoppingOrderService, ShoppingOrderItemService
from fastapi import HTTPException, Response
from app.users.exceptions import CustomerNotFoundError
from app.offices.exceptions import OfficeNotFoundError
from app.shopping_orders.exceptions import ShoppingOrderNotFoundError, ShoppingOrderTotalPriceSubtractionError, \
    DateNotValid, ShoppingOrderItemNotFoundError
from app.carts.services import ShoppingCartService, CartItemService
from app.carts.exceptions import ShoppingCartNotFoundError, CartItemNotFoundError
from app.default_values import SHIPPING_COST, TODAY_DATE_STR
from datetime import datetime


class ShoppingOrderController:
    """This class is responsible for handling all the requests related to shopping orders"""

    @staticmethod
    def create(total_price: float, shipping_cost: float, status: int, order_date: str, shipped_date: str or None,
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
        except DateNotValid as e:
            raise HTTPException(status_code=400, detail=e.message)
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
        except ShoppingOrderNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No shopping orders in system.")
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
        except DateNotValid as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ValueError:
            raise HTTPException(status_code=400, detail="Date not valid")
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
        except ShoppingOrderItemNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No items in this shopping order.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_today_shopping_orders() -> list[object]:
        try:
            shopping_orders = ShoppingOrderService.read_today_shopping_orders()
            return shopping_orders
        except ShoppingOrderNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No shopping orders for today.")
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

    @staticmethod
    def make_order(customer_id: str, office_id: str) -> object:
        try:
            # checking if inputs valid
            CustomerService.read_by_id(customer_id)
            OfficeService.read_by_id(office_id)
            shopping_cart = ShoppingCartService.read_by_customer_id(customer_id)
            # getting all cart items
            cart_items = CartItemService.read_by_shopping_cart_id(shopping_cart.shopping_cart_id)

            # checking quantity in stock
            for item in cart_items:
                product = ProductService.read_by_id(item.product_id)
                if product.quantity_in_stock < item.quantity:
                    raise HTTPException(status_code=400, detail=f"Product {product.name} is currently out of stock.")

            # making order
            shopping_order = ShoppingOrderService.create(total_price=0, shipping_cost=SHIPPING_COST, status=0,
                                                         order_date=TODAY_DATE_STR,
                                                         shipped_date=None, customer_id=customer_id,
                                                         office_id=office_id)
            total_price = SHIPPING_COST
            shopping_order.items = []

            # making items in order
            for item in cart_items:
                shopping_order.items.append(ShoppingOrderItemService.create(item.quantity, item.product_id,
                                                                            shopping_order.shopping_order_id))

                # updating quantity in stock for products
                product = ProductService.update_quantity_in_stock(item.product_id, item.quantity, subtract=True)

                # adding price to total price
                total_price += product.price * item.quantity

                # deleting cart item
                CartItemService.delete_by_id(item.cart_item_id)

            # setting cart total cost to 0
            ShoppingCartService.update_set_total_cost(shopping_cart.shopping_cart_id, 0)

            # updating total price for order
            shopping_order = ShoppingOrderService.update_total_price_for_amount(shopping_order.shopping_order_id,
                                                                                total_price)

            return shopping_order

        except OfficeNotFoundError as e:
            raise HTTPException(status_code=400, detail=e.message)
        except CartItemNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No cart items in this customer shopping cart.")
        except ShoppingCartNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except CustomerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
