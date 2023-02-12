from app.users.repositories.customer_repository import CustomerRepository
from app.db.database import SessionLocal


class CustomerService:

    @staticmethod
    def create(name: str, surname: str, phone: str, address: str, city: str, country: str, postal_code: str,
               user_id: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.create(name, surname, phone, address, city, country, postal_code, user_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(customer_id: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.read_by_id(customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.read_all()
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(customer_id: str):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.delete_by_id(customer_id)
        except Exception as e:
            raise e

    @staticmethod
    def update(customer_id: str, name: str = None, surname: str = None, phone: str = None, address: str = None,
               city: str = None, country: str = None, postal_code: str = None):
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.update(customer_id, name, surname, phone,
                                                  address, city, country, postal_code)
        except Exception as e:
            raise e
