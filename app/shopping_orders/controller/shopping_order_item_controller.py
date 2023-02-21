from app.products.services import ProductService
from app.shopping_orders.services import ShoppingOrderService, ShoppingOrderItemService
from fastapi import HTTPException, Response
from app.products.exceptions import ProductNotFoundError, ProductOutOfStockError
from app.shopping_orders.exceptions import ShoppingOrderNotFoundError, ShoppingOrderItemNotFoundError


class ShoppingOrderItemController:

    # prvo provera da li ima proizvoda na stanju, zatim create item order i onda azuriranje brojnog
    # stanja proizvoda koje je smanjeno, a zatim azuriranje total_price u shopping order
    @staticmethod
    def create(quantity: int, product_id: str, shopping_order_id: str) -> object:
        try:
            ShoppingOrderService.read_by_id(shopping_order_id)
            product = ProductService.read_by_id(product_id)
            if product.quantity_in_stock < quantity:
                raise HTTPException(status_code=ProductOutOfStockError().code, detail=ProductOutOfStockError().message)
            shopping_order_item = ShoppingOrderItemService.create(quantity, product_id, shopping_order_id)
            ProductService.update_quantity_in_stock(product_id, quantity, subtract=True)
            item_price = product.price * quantity
            ShoppingOrderService.update_total_price_for_amount(shopping_order_id, item_price)
            return shopping_order_item
        except ProductNotFoundError as e:
            raise HTTPException(status_code=400, detail=e.message)
        except ShoppingOrderNotFoundError as e:
            raise HTTPException(status_code=400, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(shopping_order_item_id: str) -> object:
        try:
            shopping_order_item = ShoppingOrderItemService.read_by_id(shopping_order_item_id)
            return shopping_order_item
        except ShoppingOrderItemNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all() -> list[object]:
        try:
            shopping_order_items = ShoppingOrderItemService.read_all()
            return shopping_order_items
        except ShoppingOrderItemNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="There is no shopping order items in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(shopping_order_item_id: str) -> Response:
        try:
            ShoppingOrderItemService.delete_by_id(shopping_order_item_id)
            return Response(status_code=200, content=f"Shopping order item with id - {shopping_order_item_id} deleted.")
        except ShoppingOrderItemNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_items_by_shopping_order_id(shopping_order_id: str) -> list[object]:
        try:
            ShoppingOrderService.read_by_id(shopping_order_id)
            shopping_order_items = ShoppingOrderItemService.read_items_by_shopping_order_id(shopping_order_id)
            return shopping_order_items
        except ShoppingOrderNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ShoppingOrderItemNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="There is no shopping order items in this order.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
