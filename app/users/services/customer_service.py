from sqlalchemy.exc import IntegrityError

from app.db.database import SessionLocal
from app.users.exceptions import CustomerNotFoundError
from app.users.repositories.customer_repository import CustomerRepository


class CustomerService:
    """Customer Service"""

    @staticmethod
    def create(
        name: str, surname: str, phone: str, address: str, city: str, country: str, postal_code: str, user_id: str
    ) -> object:
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                return customer_repository.create(name, surname, phone, address, city, country, postal_code, user_id)
        except IntegrityError as exc:
            raise exc
        except Exception as exc:
            raise exc

    @staticmethod
    def read_by_id(customer_id: str) -> object:
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                customer = customer_repository.read_by_id(customer_id)
                if customer is None:
                    raise CustomerNotFoundError()
                return customer
        except Exception as exc:
            raise exc

    @staticmethod
    def read_all() -> list[object]:
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                customers = customer_repository.read_all()
                if len(customers) == 0:
                    raise CustomerNotFoundError()
                return customers
        except Exception as exc:
            raise exc

    @staticmethod
    def delete_by_id(customer_id: str) -> bool:
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                customer = customer_repository.delete_by_id(customer_id)
                if customer is None:
                    raise CustomerNotFoundError()
            return customer
        except IntegrityError as exc:
            raise exc
        except Exception as exc:
            raise exc

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
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                customer = customer_repository.update(
                    customer_id, name, surname, phone, address, city, country, postal_code
                )
                if customer is None:
                    raise CustomerNotFoundError()
                return customer
        except Exception as exc:
            raise exc

    @staticmethod
    def read_by_user_id(user_id: str) -> object:
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                customer = customer_repository.read_by_user_id(user_id)
                if customer is None:
                    raise CustomerNotFoundError()
                return customer
        except Exception as exc:
            raise exc

    @staticmethod
    def read_customers_by_phone(phone: str) -> list[object]:
        try:
            with SessionLocal() as db:
                customer_repository = CustomerRepository(db)
                customers = customer_repository.read_customers_by_phone(phone)
                if len(customers) == 0:
                    raise CustomerNotFoundError()
                return customers
        except Exception as exc:
            raise exc
