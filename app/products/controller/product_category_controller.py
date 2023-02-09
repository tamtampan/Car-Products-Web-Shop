from app.products.services import ProductCategoryService
from fastapi import HTTPException, Response
# from app.products.exceptions import *


class ProductCategoryController:

    @staticmethod
    def create(name):
        try:
            product_category = ProductCategoryService.create(name)
            return product_category
        #
        # except EmployeeTypeExistsException as e:
        #     raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_by_id(product_category_id: str):
        try:
            product_category = ProductCategoryService.get_by_id(product_category_id)
            if product_category:
                return product_category
        # except EmployeeTypeNotFoundException as e:
        #     raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_by_name(name: str):
        try:
            product_category = ProductCategoryService.get_by_name(name)
            if product_category:
                return product_category
        # except EmployeeTypeNotFoundException as e:
        #     raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all():
        product_categories = ProductCategoryService.get_all()
        return product_categories

    @staticmethod
    def delete_by_id(product_category_id: str):
        try:
            ProductCategoryService.delete_by_id(product_category_id)
            return Response(content=f"Product category with id - {product_category_id} is deleted")
        # except EmployeeTypeNotFoundException as e:
        #     raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_name(product_category_id: str, new_name: str):
        try:
            product_category = ProductCategoryService.update_name(product_category_id, new_name)
            return product_category
        # except EmployeeTypeNotFoundException as e:
        #     raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
