from fastapi import APIRouter
from app.products.controller import ProductCategoryController
from app.products.schemas import *

product_category_router = APIRouter(tags=["Product category"], prefix="/api/product-categories")


@product_category_router.post("/add-new-product-category", response_model=ProductCategorySchemaIn)
def create_product_category(product_category: ProductCategorySchemaIn):
    return ProductCategoryController.create(product_category.name)


@product_category_router.get("/id", response_model=ProductCategorySchema)
def get_product_category_by_id(product_category_id: str):
    return ProductCategoryController.get_by_id(product_category_id)


@product_category_router.get("/name", response_model=ProductCategorySchema)
def get_product_category_by_name(name: str):
    return ProductCategoryController.get_by_name(name)


@product_category_router.get("/get-all-product-categories", response_model=list[ProductCategorySchema])
def get_all_product_categories():
    return ProductCategoryController.get_all()


@product_category_router.delete("/")
def delete_product_category_by_id(product_category_id: str):
    return ProductCategoryController.delete_by_id(product_category_id)


@product_category_router.put("/update/product-category", response_model=ProductCategorySchema)
def update_product_category_name(product_category_id: str, name: str):
    return ProductCategoryController.update_name(product_category_id, name)
