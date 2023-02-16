from sqlalchemy.exc import IntegrityError
from app.users.services import CustomerService, UserService
from fastapi import HTTPException, Response
from app.users.exceptions import CustomerNotFoundException, UserNotFoundException


class CustomerController:

    @staticmethod
    def create(name: str, surname: str, phone: str, address: str, city: str, country: str, postal_code: str,
               user_id: str):
        try:
            UserService.read_by_id(user_id)
            customer = CustomerService.create(name, surname, phone, address, city, country, postal_code, user_id)
            return customer
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User is already customer.")
        except UserNotFoundException:
            raise HTTPException(status_code=400, detail=f"You can not be customer if you are not user.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(customer_id: str):
        try:
            customer = CustomerService.read_by_id(customer_id)
            return customer
        except CustomerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all():
        try:
            customers = CustomerService.read_all()
            return customers
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(customer_id: str):
        try:
            CustomerService.delete_by_id(customer_id)
            return Response(status_code=200, content=f"Customer with id - {customer_id} deleted.")
        except CustomerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(customer_id: str, name: str = None, surname: str = None, phone: str = None, address: str = None,
               city: str = None, country: str = None, postal_code: str = None):
        try:
            customer = CustomerService.update(customer_id, name, surname, phone,
                                              address, city, country, postal_code)
            return customer
        except CustomerNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# @staticmethod
# def get_by_email(email: str):
#     pass
#     # try:
#     #     user = UserService.read_by_email(email)
#     #     customer = CustomerService.read_by_id()
#     #
#     #     return user
#     # except UserNotFoundException as e:
#     #     raise HTTPException(status_code=e.code, detail=e.message)
#     # except Exception as e:
#     #     raise HTTPException(status_code=500, detail=str(e))
