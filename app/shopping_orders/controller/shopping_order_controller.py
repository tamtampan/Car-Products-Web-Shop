from datetime import datetime

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from starlette.responses import JSONResponse

from app.carts.exceptions import CartItemNotFoundError, ShoppingCartNotFoundError
from app.carts.services import CartItemService, ShoppingCartService
from app.default_values import SHIPPING_COST, TODAY_DATE_STR
from app.offices.exceptions import OfficeNotFoundError
from app.offices.services import OfficeService
from app.products.exceptions import ProductNotFoundError, ProductOutOfStockError
from app.products.services import ProductService
from app.shopping_orders.exceptions import (
    DateNotValid,
    ShoppingOrderItemNotFoundError,
    ShoppingOrderNotFoundError,
    ShoppingOrderTotalPriceSubtractionError,
)
from app.shopping_orders.services import ShoppingOrderItemService, ShoppingOrderService
from app.users.exceptions import CustomerNotFoundError
from app.users.services import CustomerService


class ShoppingOrderController:
    """Shopping Order Controller"""

    @staticmethod
    def create(
        total_price: float,
        shipping_cost: float,
        status: int,
        order_date: str,
        shipped_date: str or None,
        customer_id: str,
        office_id: str,
    ) -> object:
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
            shopping_order = ShoppingOrderService.create(
                total_price, shipping_cost, status, order_date, shipped_date, customer_id, office_id
            )
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
            return JSONResponse(status_code=200, content=f"Shopping order with id - {shopping_order_id} deleted.")
        except ShoppingOrderNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Can not delete shopping order that has items in it.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(
        shopping_order_id: str, shipping_cost: float = None, status: int = None, shipped_date: str = None
    ) -> object:
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
        """
        "Read a shopping order by id and return it with its items."

        The function is a bit long, but it's not too bad. It's a bit hard to read because of the try/except blocks, but it's
        not too bad
        :param shopping_order_id: str
        :type shopping_order_id: str
        :return: An object
        """
        try:
            shopping_order = ShoppingOrderService.read_by_id(shopping_order_id)
            shopping_order.items = ShoppingOrderItemService.read_items_by_shopping_order_id(shopping_order_id)
            return shopping_order
        except ShoppingOrderNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except ShoppingOrderItemNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="No items in this shopping order.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_today_shopping_orders() -> list[object]:
        """
        Reads today's shopping orders
        :return: A list of shopping orders.
        """

        try:
            shopping_orders = ShoppingOrderService.read_today_shopping_orders()
            return shopping_orders
        except ShoppingOrderNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="No shopping orders for today.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def sum_today_profit() -> Response:
        """
        It returns the sum of all the profits made today
        :return: Response object
        """

        try:
            profit = ShoppingOrderService.sum_today_profit()
            return Response(status_code=200, content=f"Profit for today is {profit} dinars.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def update_total_price_for_amount(shopping_order_id: str, amount: float, subtract: bool = False) -> object:
        """
        It updates the total price of a shopping order by adding or subtracting the amount passed in
        :param shopping_order_id: str - The id of the shopping order
        :type shopping_order_id: str
        :param amount: float - the amount to be added or subtracted from the total price
        :type amount: float
        :param subtract: bool = False, defaults to False
        :type subtract: bool (optional)
        :return: The shopping order object is being returned.
        """

        try:
            shopping_order = ShoppingOrderService.update_total_price_for_amount(shopping_order_id, amount, subtract)
            return shopping_order
        except ShoppingOrderTotalPriceSubtractionError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except ShoppingOrderNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def make_order(customer_id: str, office_id: str) -> object:
        """
        It takes a customer id and an office id as input, checks if the customer and office exist, checks if the customer
        has items in their cart, checks if the quantity in stock is enough for the order, creates an order, creates order
        items, updates the quantity in stock for the products, deletes the cart items, sets the cart total cost to 0,
        updates the total price for the order, and returns the order
        :param customer_id: str, office_id: str
        :type customer_id: str
        :param office_id: str
        :type office_id: str
        :return: A shopping order object
        """

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
            shopping_order = ShoppingOrderService.create(
                total_price=0,
                shipping_cost=SHIPPING_COST,
                status=0,
                order_date=TODAY_DATE_STR,
                shipped_date=None,
                customer_id=customer_id,
                office_id=office_id,
            )
            total_price = SHIPPING_COST
            shopping_order.items = []

            # making items in order
            for item in cart_items:
                shopping_order.items.append(
                    ShoppingOrderItemService.create(item.quantity, item.product_id, shopping_order.shopping_order_id)
                )

                # updating quantity in stock for products
                product = ProductService.update_quantity_in_stock(item.product_id, item.quantity, subtract=True)

                # adding price to total price
                total_price += product.price * item.quantity

                # deleting cart item
                CartItemService.delete_by_id(item.cart_item_id)

            # setting cart total cost to 0
            ShoppingCartService.update_set_total_cost(shopping_cart.shopping_cart_id, 0)

            # updating total price for order
            shopping_order = ShoppingOrderService.update_total_price_for_amount(
                shopping_order.shopping_order_id, total_price
            )

            return shopping_order

        except OfficeNotFoundError as exc:
            raise HTTPException(status_code=400, detail=exc.message)
        except CartItemNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="No cart items in this customer shopping cart.")
        except ShoppingCartNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except CustomerNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except ProductNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
