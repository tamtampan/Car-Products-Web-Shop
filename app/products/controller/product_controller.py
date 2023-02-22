"""Product Controller Module"""

from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.products.exceptions import (
    ProducerNotFoundError,
    ProductCategoryNotFoundError,
    ProductCodeNotFoundError,
    ProductNotFoundError,
    ProductQuantityInStockSubtractionError,
)
from app.products.services import ProducerService, ProductCategoryService, ProductService


class ProductController:
    """Product Controller"""

    @staticmethod
    def create(
        name: str,
        description: str,
        code: str,
        price: float,
        for_car_brand: str,
        quantity_in_stock: int,
        producer_id: str,
        product_category_id: str,
    ) -> object:
        """Create"""
        try:
            ProducerService.read_by_id(producer_id)
            ProductCategoryService.read_by_id(product_category_id)
            product = ProductService.create(
                name, description, code, price, for_car_brand, quantity_in_stock, producer_id, product_category_id
            )
            return product
        except ProducerNotFoundError as e:
            raise HTTPException(status_code=400, detail=e.message)
        except ProductCategoryNotFoundError as e:
            raise HTTPException(status_code=400, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"Product with provided code - {code} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(product_id: str) -> object:
        """ "Read by id"""

        try:
            product = ProductService.read_by_id(product_id)
            return product
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all() -> list[object]:
        """Read all"""

        try:
            products = ProductService.read_all()
            return products
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No products in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(product_id: str) -> Response:
        """Delete by id"""

        try:
            ProductService.delete_by_id(product_id)
            return Response(status_code=200, content=f"Product with id - {product_id} deleted.")
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="First delete cart items and order items with this product.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(
        product_id: str,
        name: str = None,
        description: str = None,
        price: float = None,
        for_car_brand: str = None,
        quantity_in_stock: int = None,
    ) -> object:
        """Update"""

        try:
            product = ProductService.update(product_id, name, description, price, for_car_brand, quantity_in_stock)
            return product
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_quantity_in_stock(product_id: str, amount: int, subtract: bool = False) -> object:
        """It updates the quantity in stock of a product by amount."""

        try:
            product = ProductService.update_quantity_in_stock(product_id, amount, subtract)
            return product
        except ProductQuantityInStockSubtractionError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_products_for_car_brand(car_brand: str) -> list[object]:
        """Reads products for a given car brand."""
        try:
            products = ProductService.read_products_for_car_brand(car_brand)
            return products
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=f"No products for {car_brand} in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_products_by_category_name(product_category_name: str) -> list[object]:
        """Reads a list of products by a product category name."""

        try:
            product_category = ProductCategoryService.read_category_name_like(product_category_name)
            product_category_id = product_category.product_category_id
            products = ProductService.read_products_by_category_id(product_category_id)
            return products
        except ProductCategoryNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=f"No products for {product_category_name} in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all_products_sorted_by_price_from_lowest() -> list[object]:
        """It reads all products sorted by price from lowest."""

        try:
            products = ProductService.read_all_products_sorted_by_price_from_lowest()
            return products
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No products in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all_products_sorted_by_price_from_highest() -> list[object]:
        """It reads all products sorted by price from highest."""

        try:
            products = ProductService.read_all_products_sorted_by_price_from_highest()
            return products
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No products in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all_products_alphabetically_sorted() -> list[object]:
        """It reads all products from the database, sorts them alphabetically, and returns them."""

        try:
            products = ProductService.read_all_products_alphabetically_sorted()
            return products
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No products for in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_products_name_like(name: str) -> list[object]:
        """This function returns a list of products with names like the given name."""

        try:
            products = ProductService.read_products_name_like(name)
            return products
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=f"No products with name like {name} in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_code(code: str) -> object:
        """It reads a product by code."""

        try:
            product = ProductService.read_by_code(code)
            return product
        except ProductCodeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_products_by_descending_number_of_sold() -> list[object]:
        try:
            products = ProductService.read_products_by_descending_number_of_sold()
            return products
        except ProductNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
