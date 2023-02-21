from fastapi import APIRouter, Response, Depends

from app.shopping_orders.controller import ShoppingOrderController, ShoppingOrderItemController
from app.shopping_orders.schemas import *
from app.users.controller import JWTBearer
# dependencies=[Depends(JWTBearer("super_user"))]


shopping_order_router = APIRouter(tags=["Shopping orders"], prefix="/api/shopping-orders")


@shopping_order_router.post("/make-order", response_model=ShoppingOrderSchema)
def make_order(customer_id: str, office_id: str) -> object:
    return ShoppingOrderController.make_order(customer_id, office_id)


@shopping_order_router.post("/add-new-shopping-order", response_model=ShoppingOrderSchema)
def create_shopping_order(shopping_order: ShoppingOrderSchemaIn) -> object:
    return ShoppingOrderController.create(shopping_order.total_price, shopping_order.shipping_cost,
                                          shopping_order.status, shopping_order.order_date,
                                          shopping_order.shipped_date, shopping_order.customer_id,
                                          shopping_order.office_id)


@shopping_order_router.get("/id", response_model=ShoppingOrderSchema)
def get_shopping_order_by_id(shopping_order_id: str) -> object:
    return ShoppingOrderController.read_by_id(shopping_order_id)


@shopping_order_router.get("/get-all-shopping-orders", response_model=list[ShoppingOrderSchema])
def get_all_shopping_orders() -> list[object]:
    return ShoppingOrderController.read_all()


@shopping_order_router.delete("/")
def delete_shopping_order_by_id(shopping_order_id: str) -> Response:
    return ShoppingOrderController.delete_by_id(shopping_order_id)


@shopping_order_router.put("/update/shopping-order", response_model=ShoppingOrderSchema)
def update_shopping_order(shopping_order_id: str, shipping_cost: float = None, status: int = None,
                          shipped_date: str = None) -> object:
    return ShoppingOrderController.update(shopping_order_id, shipping_cost, status, shipped_date)


@shopping_order_router.get("/shopping-order-with-items", response_model=ShoppingOrderSchemaOut)
def get_shopping_order_with_items(shopping_order_id: str) -> object:
    return ShoppingOrderController.read_shopping_order_with_items(shopping_order_id)


@shopping_order_router.get("/get-today-shopping-orders", response_model=list[ShoppingOrderSchema])
def get_today_shopping_orders() -> list[object]:
    return ShoppingOrderController.read_today_shopping_orders()


@shopping_order_router.get("/sum-today-profit", response_model=float)
def sum_today_profit() -> Response:
    return ShoppingOrderController.sum_today_profit()


# treba da se uradi nakon sto se definisu svi shopping item-i
@shopping_order_router.put("/update/total_price", response_model=ShoppingOrderSchema)
def update_sum_total_price(shopping_order_id: str) -> object:
    return ShoppingOrderController.update_sum_total_price(shopping_order_id)


@shopping_order_router.put("/update/total_price_for_amount", response_model=ShoppingOrderSchema)
def update_total_price_for_amount(shopping_order_id: str, amount: float, subtract: bool = False) -> object:
    return ShoppingOrderController.update_total_price_for_amount(shopping_order_id, amount, subtract)


shopping_order_item_router = APIRouter(tags=["Shopping order items"], prefix="/api/shopping-order-items")


@shopping_order_item_router.post("/add-new-shopping-order-item", response_model=ShoppingOrderItemSchema)
def create_shopping_order_item(shopping_order_item: ShoppingOrderItemSchemaIn) -> object:
    return ShoppingOrderItemController.create(shopping_order_item.quantity, shopping_order_item.product_id,
                                              shopping_order_item.shopping_order_id)


@shopping_order_item_router.get("/id", response_model=ShoppingOrderItemSchema)
def get_shopping_order_item_by_id(shopping_order_item_id: str) -> object:
    return ShoppingOrderItemController.read_by_id(shopping_order_item_id)


@shopping_order_item_router.get("/get-all-shopping-order-items", response_model=list[ShoppingOrderItemSchema])
def get_all_shopping_order_items() -> list[object]:
    return ShoppingOrderItemController.read_all()


@shopping_order_item_router.delete("/")
def delete_shopping_order_item_by_id(shopping_order_item_id: str) -> Response:
    return ShoppingOrderItemController.delete_by_id(shopping_order_item_id)


@shopping_order_item_router.get("/get-items-by-shopping-order-id", response_model=list[ShoppingOrderItemSchema])
def get_items_by_shopping_order_id(shopping_order_id: str) -> list[object]:
    return ShoppingOrderItemController.read_items_by_shopping_order_id(shopping_order_id)
