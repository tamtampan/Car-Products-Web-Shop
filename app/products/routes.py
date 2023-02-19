from fastapi import APIRouter, Response
from app.products.controller import ProductCategoryController, ProducerController, ProductController
from app.products.schemas import *

product_category_router = APIRouter(tags=["Product categories"], prefix="/api/product-categories")


@product_category_router.post("/add-new-product-category", response_model=ProductCategorySchema)
def create_product_category(product_category: ProductCategorySchemaIn) -> object:
    return ProductCategoryController.create(product_category.name)


@product_category_router.get("/id", response_model=ProductCategorySchema)
def get_product_category_by_id(product_category_id: str) -> object:
    return ProductCategoryController.read_by_id(product_category_id)


@product_category_router.get("/name", response_model=ProductCategorySchema)
def get_product_category_by_name(name: str) -> object:
    return ProductCategoryController.read_by_name(name)


@product_category_router.get("/get-all-product-categories", response_model=list[ProductCategorySchema])
def get_all_product_categories() -> list[object]:
    return ProductCategoryController.read_all()


@product_category_router.delete("/")
def delete_product_category_by_id(product_category_id: str) -> Response:
    return ProductCategoryController.delete_by_id(product_category_id)


@product_category_router.put("/update/product-category", response_model=ProductCategorySchema)
def update_product_category_name(product_category_id: str, name: str) -> object:
    return ProductCategoryController.update_name(product_category_id, name)


@product_category_router.get("/category-like-name", response_model=ProductCategorySchema)
def get_category_name_like(name: str) -> object:
    return ProductCategoryController.read_category_name_like(name)


producer_router = APIRouter(tags=["Producers"], prefix="/api/producers")


@producer_router.post("/add-new-producer", response_model=ProducerSchema)
def create_producer(producer: ProducerSchemaIn) -> object:
    return ProducerController.create(producer.name, producer.address, producer.description)


@producer_router.get("/id", response_model=ProducerSchema)
def get_producer_by_id(producer_id: str) -> object:
    return ProducerController.read_by_id(producer_id)


@producer_router.get("/name", response_model=ProducerSchema)
def get_producer_by_name(name: str) -> object:
    return ProducerController.read_by_name(name)


@producer_router.get("/get-all-producers", response_model=list[ProducerSchema])
def get_all_producers() -> list[object]:
    return ProducerController.read_all()


@producer_router.delete("/")
def delete_producer_by_id(producer_id: str) -> Response:
    return ProducerController.delete_by_id(producer_id)


@producer_router.put("/update/producer", response_model=ProducerSchema)
def update_producer(producer_id: str, name: str = None, address: str = None, description: str = None) -> object:
    return ProducerController.update(producer_id, name, address, description)


product_router = APIRouter(tags=["Products"], prefix="/api/products")


@product_router.post("/create-new-product", response_model=ProductSchema)
def create_product(product: ProductSchemaIn) -> object:
    return ProductController.create(product.name, product.description, product.code, product.price,
                                    product.for_car_brand, product.quantity_in_stock, product.producer_id,
                                    product.product_category_id)


@product_router.get("/id", response_model=ProductSchema)
def get_product_by_id(product_id: str) -> object:
    return ProductController.read_by_id(product_id)


@product_router.get("/get-all-products", response_model=list[ProductSchema])
def get_all_products() -> list[object]:
    return ProductController.read_all()


@product_router.delete("/")
def delete_product_by_id(product_id: str) -> Response:
    return ProductController.delete_by_id(product_id)


@product_router.put("/update/product", response_model=ProductSchema)
def update_product(product_id: str, name: str = None, description: str = None, price: float = None,
                   for_car_brand: str = None, quantity_in_stock: int = None) -> object:
    return ProductController.update(product_id, name, description, price, for_car_brand, quantity_in_stock)


@product_router.put("/update/product-quantity-in-stock", response_model=ProductSchema)
def update_product_quantity_in_stock(product_id: str, amount: int, subtract: bool = False) -> object:
    return ProductController.update_quantity_in_stock(product_id, amount, subtract)


@product_router.get("/get-products-for-car-brand", response_model=list[ProductSchema])
def get_products_for_car_brand(car_brand: str) -> list[object]:
    return ProductController.read_products_for_car_brand(car_brand)


@product_router.get("/get-products-by-category-name", response_model=list[ProductSchema])
def get_products_by_category_name(category_name: str) -> list[object]:
    return ProductController.read_products_by_category_name(category_name)


@product_router.get("/get-all-products-sorted-by-price-from-lowest", response_model=list[ProductSchema])
def get_all_products_sorted_by_price_from_lowest() -> list[object]:
    return ProductController.read_all_products_sorted_by_price_from_lowest()


@product_router.get("/get-all-products-sorted-by-price-from-highest", response_model=list[ProductSchema])
def get_all_products_sorted_by_price_from_highest() -> list[object]:
    return ProductController.read_all_products_sorted_by_price_from_highest()


@product_router.get("/get-all-products-alphabetically-sorted", response_model=list[ProductSchema])
def get_all_products_alphabetically_sorted() -> list[object]:
    return ProductController.read_all_products_alphabetically_sorted()


@product_router.get("/get-products-name-like", response_model=list[ProductSchema])
def get_products_name_like(name: str) -> list[object]:
    return ProductController.read_products_name_like(name)


@product_router.get("/code", response_model=ProductSchema)
def read_by_code(code: str) -> object:
    return ProductController.read_by_code(code)
