from sqlalchemy.exc import IntegrityError
from app.products.services import ProductService, ProducerService, ProductCategoryService
from fastapi import HTTPException, Response
from app.products.exceptions import ProducerNotFoundException, ProductCategoryNotFoundException, \
    ProductNotFoundException


class ProductController:

    @staticmethod
    def create(name: str, description: str, code: str, price: float, for_car_brand: str,
               quantity_in_stock: int, producer_id: str, product_category_id: str):
        try:
            ProducerService.read_by_id(producer_id)
            ProductCategoryService.read_by_id(product_category_id)
            product = ProductService.create(name, description, code, price, for_car_brand, quantity_in_stock,
                                            producer_id, product_category_id)
            return product
        except ProducerNotFoundException as e:
            raise HTTPException(status_code=400, detail=e.message)
        except ProductCategoryNotFoundException as e:
            raise HTTPException(status_code=400, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Product with provided code - {code} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_by_id(product_id: str):
        try:
            product = ProductService.read_by_id(product_id)
            return product
        except ProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all():
        try:
            products = ProductService.read_all()
            return products
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(product_id: str):
        try:
            ProductService.delete_by_id(product_id)
            return Response(status_code=200, content=f"Product with id - {product_id} deleted.")
        except ProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(product_id: str, name: str = None, description: str = None, price: float = None,
               for_car_brand: str = None, quantity_in_stock: int = None):
        try:
            product = ProductService.update(product_id, name, description, price, for_car_brand, quantity_in_stock)
            return product
        except ProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_quantity_in_stock(product_id: str, amount: int, subtract: bool = False):
        try:
            product = ProductService.update_quantity_in_stock(product_id, amount, subtract)
            return product
        except ProductNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
