"""Routes module"""

from fastapi import APIRouter, Depends, Response

from app.carts.controller import CartItemController, ShoppingCartController
from app.carts.schemas import (
    CartItemSchema,
    CartItemSchemaIn,
    CartItemSchemaInCustomer,
    CartItemSchemaUpdate,
    ShoppingCartSchema,
    ShoppingCartSchemaIn,
    ShoppingCartSchemaUpdate,
)
from app.users.controller import JWTBearer

shopping_cart_router = APIRouter(tags=["Shopping carts"], prefix="/api/shopping-carts")


@shopping_cart_router.post(
    "/add-new-shopping-cart", response_model=ShoppingCartSchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def create_shopping_cart(shopping_cart: ShoppingCartSchemaIn) -> object:
    """Create shopping cart"""
    return ShoppingCartController.create(shopping_cart.customer_id)


@shopping_cart_router.get("/shopping-cart-id", response_model=ShoppingCartSchema)
def get_shopping_cart_by_id(shopping_cart_id: str) -> object:
    """Get by id"""
    return ShoppingCartController.read_by_id(shopping_cart_id)


@shopping_cart_router.get("/shopping-cart-customer-id", response_model=ShoppingCartSchema)
def get_cart_by_customer_id(customer_id: str) -> object:
    """Get by customer id"""
    return ShoppingCartController.read_by_customer_id(customer_id)


@shopping_cart_router.get(
    "/get-all-shopping-carts", response_model=list[ShoppingCartSchema], dependencies=[Depends(JWTBearer("super_user"))]
)
def get_all_shopping_carts() -> list[object]:
    """Get all"""
    return ShoppingCartController.read_all()


@shopping_cart_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_shopping_cart_by_id(shopping_cart_id: str) -> Response:
    """Delete by id"""
    return ShoppingCartController.delete_by_id(shopping_cart_id)


@shopping_cart_router.put(
    "/update/total-cost", response_model=ShoppingCartSchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def update_shopping_cart(cart: ShoppingCartSchemaUpdate) -> object:
    """Update"""
    return ShoppingCartController.update(cart.shopping_cart_id, cart.amount, cart.subtract)


cart_item_router = APIRouter(tags=["Cart items"], prefix="/api/cart_items")


@cart_item_router.post("/add-new-cart-item-by-customer-id", response_model=CartItemSchema)
def create_cart_item_by_customer_id(item: CartItemSchemaInCustomer) -> object:
    """Create with customer id"""

    return CartItemController.create_by_customer_id(item.quantity, item.customer_id, item.product_id)


@cart_item_router.post(
    "/add-new-cart-item", response_model=CartItemSchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def create_cart_item(item: CartItemSchemaIn) -> object:
    """Create"""
    return CartItemController.create(item.quantity, item.shopping_cart_id, item.product_id)


@cart_item_router.get("/id", response_model=CartItemSchema)
def get_cart_item_by_id(cart_item_id: str) -> object:
    """Get by id"""
    return CartItemController.read_by_id(cart_item_id)


@cart_item_router.get(
    "/get-all-cart-items", response_model=list[CartItemSchema], dependencies=[Depends(JWTBearer("super_user"))]
)
def get_all_cart_items() -> list[object]:
    """Get all"""
    return CartItemController.read_all()


@cart_item_router.get("/get-all-cart-items-for-shopping-cart", response_model=list[CartItemSchema])
def get_all_cart_items_for_shopping_cart(shopping_cart_id: str) -> list[object]:
    """Get all for one cart"""
    return CartItemController.read_by_shopping_cart_id(shopping_cart_id)


@cart_item_router.delete("/")
def delete_cart_item_by_id(cart_item_id: str) -> Response:
    """Delete by id"""
    return CartItemController.delete_by_id(cart_item_id)


@cart_item_router.put("/update/quantity", response_model=CartItemSchema)
def update_cart_item_quantity(cart_item: CartItemSchemaUpdate) -> object:
    """Update quantity"""
    return CartItemController.update_quantity(cart_item.cart_item_id, cart_item.quantity)
