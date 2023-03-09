"""Product Category Controller Module"""

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.products.exceptions import *
from app.products.services import ProductCategoryService
from starlette.responses import JSONResponse


class ProductCategoryController:
    """Product Category Controller"""

    @staticmethod
    def create(name: str) -> object:
        """
        It creates a product category with the given name
        :param name: str - the name of the product category
        :type name: str
        :return: The product category object is being returned.
        """
        try:
            product_category = ProductCategoryService.create(name)
            return product_category
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Product category with provided name - {name} already exists.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_by_id(product_category_id: str) -> object:
        """Read by id"""

        try:
            product_category = ProductCategoryService.read_by_id(product_category_id)
            if product_category:
                return product_category
        except ProductCategoryNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_by_name(name: str) -> object:
        """It reads a product category by name."""
        try:
            product_category = ProductCategoryService.read_by_name(name)
            if product_category:
                return product_category
        except ProductCategoryNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_all() -> list[object]:
        """Read all"""

        try:
            product_categories = ProductCategoryService.read_all()
            return product_categories
        except ProductCategoryNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="No product categories in system.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def delete_by_id(product_category_id: str) -> Response:
        """Delete by id"""

        try:
            ProductCategoryService.delete_by_id(product_category_id)
            return JSONResponse(content=f"Product category with id - {product_category_id} is deleted")
        except ProductCategoryNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Can not delete product category with existing products.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def update_name(product_category_id: str, new_name: str) -> object:
        """It updates the name of a product category."""
        try:
            product_category = ProductCategoryService.update_name(product_category_id, new_name)
            return product_category
        except ProductCategoryNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_category_name_like(name: str) -> object:
        """It reads a product category by name or by initial letters."""

        try:
            product_category = ProductCategoryService.read_category_name_like(name)
            return product_category
        except ProductCategoryNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
