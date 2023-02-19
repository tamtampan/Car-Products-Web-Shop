from sqlalchemy.exc import IntegrityError
from app.users.services import CustomerService, UserService
from fastapi import HTTPException, Response
from app.users.exceptions import CustomerNotFoundError, UserNotFoundError


class CustomerController:

    @staticmethod
    def create(name: str, surname: str, phone: str, address: str, city: str, country: str, postal_code: str,
               user_id: str) -> object:
        try:
            UserService.read_by_id(user_id)
            customer = CustomerService.create(name, surname, phone, address, city, country, postal_code, user_id)
            return customer
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User is already customer.")
        except UserNotFoundError:
            raise HTTPException(status_code=400, detail=f"You can not be customer if you are not user.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(customer_id: str) -> object:
        try:
            customer = CustomerService.read_by_id(customer_id)
            return customer
        except CustomerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all() -> list[object]:
        try:
            customers = CustomerService.read_all()
            return customers
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(customer_id: str) -> Response:
        try:
            CustomerService.delete_by_id(customer_id)
            return Response(status_code=200, content=f"Customer with id - {customer_id} deleted.")
        except CustomerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Can not create customer that has shopping orders and "
                                                        "shopping cart.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(customer_id: str, name: str = None, surname: str = None, phone: str = None, address: str = None,
               city: str = None, country: str = None, postal_code: str = None) -> object:
        try:
            customer = CustomerService.update(customer_id, name, surname, phone,
                                              address, city, country, postal_code)
            return customer
        except CustomerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_email(email: str) -> object:
        try:
            user = UserService.read_by_email(email)
            user_id = user.user_id
            customer = CustomerService.read_by_user_id(user_id)
            return customer
        except UserNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="User with provided email not found.")
        except CustomerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="Customer with provided email does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_customers_by_phone(phone: str) -> list[object]:
        try:
            customers = CustomerService.read_customers_by_phone(phone)
            return customers
        except CustomerNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No customers with provided phone number.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
