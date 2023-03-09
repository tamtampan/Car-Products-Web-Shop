"""Routes for Product categories"""

from fastapi import APIRouter, Depends, Response

from app.products.controller import ProducerController, ProductCategoryController, ProductController
from app.products.schemas import *
from app.users.controller import JWTBearer

product_category_router = APIRouter(tags=["Product categories"], prefix="/api/product-categories")


@product_category_router.post(
    "/add-new-product-category", response_model=ProductCategorySchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def create_product_category(product_category: ProductCategorySchemaIn) -> object:
    """Create Product category"""
    return ProductCategoryController.create(product_category.name)


@product_category_router.get("/id", response_model=ProductCategorySchema)
def get_product_category_by_id(product_category_id: str) -> object:
    """Get by id"""
    return ProductCategoryController.read_by_id(product_category_id)


@product_category_router.get("/name", response_model=ProductCategorySchema)
def get_product_category_by_name(name: str) -> object:
    """Get by name"""
    return ProductCategoryController.read_by_name(name)


@product_category_router.get("/get-all-product-categories", response_model=list[ProductCategorySchema])
def get_all_product_categories() -> list[object]:
    """Get all"""
    return ProductCategoryController.read_all()


@product_category_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_product_category_by_id(product_category_id: str) -> Response:
    """Delete by id"""
    return ProductCategoryController.delete_by_id(product_category_id)


@product_category_router.put(
    "/update/product-category", response_model=ProductCategorySchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def update_product_category_name(product_category: ProductCategorySchemaUpdate) -> object:
    """Update"""
    return ProductCategoryController.update_name(product_category.product_category_id, product_category.name)


@product_category_router.get("/category-like-name", response_model=ProductCategorySchema)
def get_category_name_like(name: str) -> object:
    """Get by name or initial letters"""
    return ProductCategoryController.read_category_name_like(name)


producer_router = APIRouter(tags=["Producers"], prefix="/api/producers")


@producer_router.post(
    "/add-new-producer", response_model=ProducerSchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def create_producer(producer: ProducerSchemaIn) -> object:
    """Create producer"""
    return ProducerController.create(producer.name, producer.address, producer.description)


@producer_router.get("/id", response_model=ProducerSchema)
def get_producer_by_id(producer_id: str) -> object:
    """Get by id"""
    return ProducerController.read_by_id(producer_id)


@producer_router.get("/name", response_model=ProducerSchema)
def get_producer_by_name(name: str) -> object:
    """Get by name"""
    return ProducerController.read_by_name(name)


@producer_router.get("/get-all-producers", response_model=list[ProducerSchema])
def get_all_producers() -> list[object]:
    """Get all"""
    return ProducerController.read_all()


@producer_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_producer_by_id(producer_id: str) -> Response:
    """Delete"""
    return ProducerController.delete_by_id(producer_id)


@producer_router.put("/update/producer", response_model=ProducerSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_producer(producer: ProducerSchemaUpdate) -> object:
    """Update"""
    return ProducerController.update(
        producer_id=producer.producer_id, name=producer.name, address=producer.address, description=producer.description
    )


product_router = APIRouter(tags=["Products"], prefix="/api/products")


@product_router.post(
    "/create-new-product", response_model=ProductSchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def create_product(product: ProductSchemaIn) -> object:
    """Create Product"""
    return ProductController.create(
        product.name,
        product.description,
        product.code,
        product.price,
        product.for_car_brand,
        product.quantity_in_stock,
        product.producer_id,
        product.product_category_id,
    )


@product_router.get("/id", response_model=ProductSchema)
def get_product_by_id(product_id: str) -> object:
    """Get by id"""
    return ProductController.read_by_id(product_id)


@product_router.get("/get-all-products", response_model=list[ProductSchema])
def get_all_products() -> list[object]:
    """Get all"""
    return ProductController.read_all()


@product_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_product_by_id(product_id: str) -> Response:
    """Delete by id"""
    return ProductController.delete_by_id(product_id)


@product_router.put("/update/product", response_model=ProductSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_product(product: ProductSchemaUpdate) -> object:
    """Update"""
    return ProductController.update(
        product.product_id,
        product.name,
        product.description,
        product.price,
        product.for_car_brand,
        product.quantity_in_stock,
    )


@product_router.put(
    "/update/product-quantity-in-stock", response_model=ProductSchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def update_product_quantity_in_stock(product: ProductSchemaUpdateQuantity) -> object:
    """Update quantity in stock"""
    return ProductController.update_quantity_in_stock(product.product_id, product.amount, product.subtract)


@product_router.get("/get-products-for-car-brand", response_model=list[ProductSchema])
def get_products_for_car_brand(car_brand: str) -> list[object]:
    """Get by brand"""
    return ProductController.read_products_for_car_brand(car_brand)


@product_router.get("/get-products-by-category-name", response_model=list[ProductSchema])
def get_products_by_category_name(category_name: str) -> list[object]:
    """Get by category"""
    return ProductController.read_products_by_category_name(category_name)


@product_router.get("/get-all-products-sorted-by-price-from-lower", response_model=list[ProductSchema])
def get_all_products_sorted_by_price_from_lower() -> list[object]:
    """Get from lower price"""
    return ProductController.read_all_products_sorted_by_price_from_lowest()


@product_router.get("/get-all-products-sorted-by-price-from-higher", response_model=list[ProductSchema])
def get_all_products_sorted_by_price_from_higher() -> list[object]:
    """Get from higher price"""
    return ProductController.read_all_products_sorted_by_price_from_highest()


@product_router.get("/get-all-products-alphabetically-sorted", response_model=list[ProductSchema])
def get_all_products_alphabetically_sorted() -> list[object]:
    """Get all alphabetically sorted"""
    return ProductController.read_all_products_alphabetically_sorted()


@product_router.get("/get-products-name-like", response_model=list[ProductSchema])
def get_products_name_like(name: str) -> list[object]:
    """Get by initial letters"""
    return ProductController.read_products_name_like(name)


@product_router.get("/code", response_model=ProductSchema)
def get_by_code(code: str) -> object:
    """Get by code"""
    return ProductController.read_by_code(code)


@product_router.get("/get-products-by-descending-number-of-sold", response_model=list[ProductSchemaCount])
def get_products_by_descending_number_of_sold() -> list[object]:
    return ProductController.read_products_by_descending_number_of_sold()
