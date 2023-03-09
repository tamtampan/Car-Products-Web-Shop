from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError
from starlette.responses import JSONResponse

from app.carts.services import ShoppingCartService
from app.users.exceptions import CustomerNotFoundError, UserNotFoundError
from app.users.services import CustomerService, UserService


class CustomerController:
    """Customer Controller"""

    @staticmethod
    def create(
        name: str, surname: str, phone: str, address: str, city: str, country: str, postal_code: str, user_id: str
    ) -> object:
        try:
            UserService.read_by_id(user_id)
            customer = CustomerService.create(name, surname, phone, address, city, country, postal_code, user_id)
            return customer
        except IntegrityError:
            raise HTTPException(status_code=400, detail="User is already customer.")
        except UserNotFoundError:
            raise HTTPException(status_code=400, detail="You can not be customer if you are not user.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def create_customer_with_shopping_cart(
        name: str, surname: str, phone: str, address: str, city: str, country: str, postal_code: str, user_id: str
    ) -> object:
        """Creates a customer and a shopping cart."""

        try:
            UserService.read_by_id(user_id)
            customer = CustomerService.create(name, surname, phone, address, city, country, postal_code, user_id)
            customer.cart = ShoppingCartService.create(customer.customer_id)
            return customer
        except IntegrityError:
            raise HTTPException(status_code=400, detail="User is already customer.")
        except UserNotFoundError:
            raise HTTPException(status_code=400, detail="You can not be customer if you are not user.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_by_id(customer_id: str) -> object:
        try:
            customer = CustomerService.read_by_id(customer_id)
            return customer
        except CustomerNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_all() -> list[object]:
        try:
            customers = CustomerService.read_all()
            return customers
        except CustomerNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="No customers in system.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def delete_by_id(customer_id: str) -> Response:
        try:
            CustomerService.delete_by_id(customer_id)
            return JSONResponse(status_code=200, content=f"Customer with id - {customer_id} deleted.")
        except CustomerNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except IntegrityError:
            raise HTTPException(
                status_code=400, detail="Can not delete customer that has shopping orders and " "shopping cart."
            )
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def update(
        customer_id: str,
        name: str = None,
        surname: str = None,
        phone: str = None,
        address: str = None,
        city: str = None,
        country: str = None,
        postal_code: str = None,
    ) -> object:
        try:
            customer = CustomerService.update(customer_id, name, surname, phone, address, city, country, postal_code)
            return customer
        except CustomerNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_by_email(email: str) -> object:
        """It reads a customer by email."""

        try:
            user = UserService.read_by_email(email)
            user_id = user.user_id
            customer = CustomerService.read_by_user_id(user_id)
            return customer
        except UserNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="User with provided email not found.")
        except CustomerNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="Customer with provided email does not exist.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_customers_by_phone(phone: str) -> list[object]:
        """It reads customers by phone number and returns a list of customers."""

        try:
            customers = CustomerService.read_customers_by_phone(phone)
            return customers
        except CustomerNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="No customers with provided phone number.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
