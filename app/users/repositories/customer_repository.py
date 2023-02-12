from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import Customer
from app.users.exceptions import CustomerNotFoundException


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, surname: str, phone: str, address: str, city: str, country: str, postal_code: str,
               user_id: str):
        try:
            customer = Customer(name, surname, phone, address, city, country, postal_code, user_id)
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_by_id(self, customer_id: str):
        customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
        if customer is None:
            raise CustomerNotFoundException(f"Customer with provided id: {customer_id} not found.", 400)
        return customer

    def read_all(self):
        customers = self.db.query(Customer).all()
        return customers

    def delete_by_id(self, customer_id: str):
        try:
            customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
            if customer is None:
                raise CustomerNotFoundException(f"Customer with provided id: {customer_id} not found.", 400)
            self.db.delete(customer)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self, customer_id: str, name: str = None, surname: str = None, phone: str = None, address: str = None,
               city: str = None, country: str = None, postal_code: str = None):
        try:
            customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
            if customer is None:
                raise CustomerNotFoundException(f"Customer with provided id: {customer_id} not found.", 400)
            if name is not None:
                customer.name = name
            if surname is not None:
                customer.surname = surname
            if phone is not None:
                customer.phone = phone
            if address is not None:
                customer.address = address
            if city is not None:
                customer.city = city
            if country is not None:
                customer.country = country
            if postal_code is not None:
                customer.postal_code = postal_code
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except Exception as e:
            raise e
