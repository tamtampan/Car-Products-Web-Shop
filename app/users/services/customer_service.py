from app.users.repositories.customer_repository import CustomerRepository
from app.db.database import SessionLocal


class CustomerService:

    @staticmethod
    def create(name, surname, phone, address, city, country, postal_code, user_id):
        with SessionLocal() as db:
            try:
                customer_repository = CustomerRepository(db)
                return customer_repository.create(name, surname, phone, address, city, country, postal_code, user_id)
            except Exception as e:
                raise e

