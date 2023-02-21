from fastapi import APIRouter, Depends
from app.carts.controller import ShoppingCartController, CartItemController
from app.carts.schemas import *
from fastapi import Response
from app.users.controller import JWTBearer

# dependencies=[Depends(JWTBearer("super_user"))]


shopping_cart_router = APIRouter(tags=["Shopping carts"], prefix="/api/shopping-carts")


@shopping_cart_router.post("/add-new-shopping-cart", response_model=ShoppingCartSchema)
def create_shopping_cart(shopping_cart: ShoppingCartSchemaIn) -> object:
    return ShoppingCartController.create(shopping_cart.customer_id)


@shopping_cart_router.get("/shopping-cart-id", response_model=ShoppingCartSchema)
def get_shopping_cart_by_id(shopping_cart_id: str) -> object:
    return ShoppingCartController.read_by_id(shopping_cart_id)


@shopping_cart_router.get("/shopping-cart-customer-id", response_model=ShoppingCartSchema)
def get_cart_by_customer_id(customer_id: str) -> object:
    return ShoppingCartController.read_by_customer_id(customer_id)


@shopping_cart_router.get("/get-all-shopping-carts", response_model=list[ShoppingCartSchema])
def get_all_shopping_carts() -> list[object]:
    return ShoppingCartController.read_all()


@shopping_cart_router.delete("/")
def delete_shopping_cart_by_id(shopping_cart_id: str) -> Response:
    return ShoppingCartController.delete_by_id(shopping_cart_id)


@shopping_cart_router.put("/update/total-cost", response_model=ShoppingCartSchema)
def update_shopping_cart(shopping_cart_id: str, amount: float, subtract: bool = False) -> object:
    return ShoppingCartController.update(shopping_cart_id, amount, subtract)


# @shopping_cart_router.put("/update/set-total-cost", response_model=ShoppingCartSchema)
# def update_set_total_cost(shopping_cart_id: str, total_cost: float) -> object:
#     return ShoppingCartController.update_set_total_cost(shopping_cart_id, total_cost)


cart_item_router = APIRouter(tags=["Cart items"], prefix="/api/cart_items")


# dependencies=[Depends(JWTBearer("super_user"))]


@cart_item_router.post("/add-new-cart-item-by-customer-id", response_model=CartItemSchema)
def create_cart_item_by_customer_id(quantity: int, customer_id: str, product_id: str) -> object:
    return CartItemController.create_by_customer_id(quantity, customer_id, product_id)


@cart_item_router.post("/add-new-cart-item", response_model=CartItemSchema)
def create_cart_item(cart_item: CartItemSchemaIn) -> object:
    return CartItemController.create(cart_item.quantity, cart_item.shopping_cart_id, cart_item.product_id)


@cart_item_router.get("/id", response_model=CartItemSchema)
def get_cart_item_by_id(cart_item_id: str) -> object:
    return CartItemController.read_by_id(cart_item_id)


@cart_item_router.get("/get-all-cart-items", response_model=list[CartItemSchema])
def get_all_cart_items() -> list[object]:
    return CartItemController.read_all()


@cart_item_router.get("/get-all-cart-items-for-shopping-cart", response_model=list[CartItemSchema])
def get_all_cart_items_for_shopping_cart(shopping_cart_id: str) -> list[object]:
    return CartItemController.read_by_shopping_cart_id(shopping_cart_id)


@cart_item_router.delete("/")
def delete_cart_items_by_id(cart_item_id: str) -> Response:
    return CartItemController.delete_by_id(cart_item_id)


@cart_item_router.put("/update/quantity", response_model=CartItemSchema)
def update_cart_item_quantity(cart_item_id: str, quantity: int) -> object:
    return CartItemController.update_quantity(cart_item_id, quantity)
