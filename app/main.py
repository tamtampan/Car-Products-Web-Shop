import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import engine, Base
from app.users.routes import user_router, customer_router, employee_router
from app.products.routes import product_category_router, producer_router, product_router
from app.offices.routes import office_router
from app.carts.routes import shopping_cart_router, cart_item_router

Base.metadata.create_all(bind=engine)


def init_app():
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

    return web_app


app = init_app()


@app.get("/", include_in_schema=False)
def interface():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app)
