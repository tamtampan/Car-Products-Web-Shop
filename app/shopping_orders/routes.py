from fastapi import APIRouter
from app.shopping_orders.controller import ShoppingOrderController
from app.shopping_orders.schemas import *

shopping_order_router = APIRouter(tags=["Shopping orders"], prefix="/api/shopping-orders")


@shopping_order_router.post("/add-new-shopping-order", response_model=ShoppingOrderSchema)
def create_shopping_order(shopping_order: ShoppingOrderSchemaIn):
    return ShoppingOrderController.create(shopping_order.total_price, shopping_order.status, shopping_order.order_date,
                                          shopping_order.shipped_date, shopping_order.customer_id,
                                          shopping_order.office_id)


@shopping_order_router.get("/id", response_model=ShoppingOrderSchema)
def get_shopping_order_by_id(shopping_order_id: str):
    return ShoppingOrderController.read_by_id(shopping_order_id)


@shopping_order_router.get("/get-all-shopping-orders", response_model=list[ShoppingOrderSchema])
def get_all_shopping_orders():
    return ShoppingOrderController.read_all()


@shopping_order_router.delete("/")
def delete_shopping_order_by_id(shopping_order_id: str):
    return ShoppingOrderController.delete_by_id(shopping_order_id)


@shopping_order_router.put("/update/shopping-order", response_model=ShoppingOrderSchema)
def update_shopping_order(shopping_order_id: str, status: int = None, shipped_date: date = None):
    return ShoppingOrderController.update(shopping_order_id, status, shipped_date)
