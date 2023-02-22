"""Main module"""

import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.carts.routes import cart_item_router, shopping_cart_router
from app.db.database import Base, engine
from app.offices.routes import office_router
from app.products.routes import producer_router, product_category_router, product_router
from app.shopping_orders.routes import shopping_order_item_router, shopping_order_router
from app.users.routes import customer_router, employee_router, user_router

Base.metadata.create_all(bind=engine)


def init_app():
    """Collects all routes"""

    web_app = FastAPI()
    web_app.include_router(user_router)
    web_app.include_router(product_category_router)
    web_app.include_router(office_router)
    web_app.include_router(producer_router)
    web_app.include_router(customer_router)
    web_app.include_router(employee_router)
    web_app.include_router(shopping_cart_router)
    web_app.include_router(product_router)
    web_app.include_router(cart_item_router)
    web_app.include_router(shopping_order_router)
    web_app.include_router(shopping_order_item_router)

    return web_app


app = init_app()


@app.get("/", include_in_schema=False)
def interface():
    """Adds suffix /docs to create interface"""

    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
