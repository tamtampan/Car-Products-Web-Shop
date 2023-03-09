from sqlalchemy.orm import Session

from app.users.models import Customer


class CustomerRepository:
    """Customer Repository"""

    def __init__(self, db: Session):
        self.db = db

    def create(
        self, name: str, surname: str, phone: str, address: str, city: str, country: str, postal_code: str, user_id: str
    ) -> object:
        try:
            customer = Customer(name, surname, phone, address, city, country, postal_code, user_id)
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except Exception as exc:
            raise exc

    def read_by_id(self, customer_id: str) -> object:
        try:
            customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
            return customer
        except Exception as exc:
            raise exc

    def read_all(self) -> list[object]:
        try:
            customers = self.db.query(Customer).all()
            return customers
        except Exception as exc:
            raise exc

    def delete_by_id(self, customer_id: str) -> bool or None:
        try:
            customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
            if customer is None:
                return None
            self.db.delete(customer)
            self.db.commit()
            return True
        except Exception as exc:
            raise exc

    def update(
        self,
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
            customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
            if customer is None:
                return None
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
        except Exception as exc:
            raise exc

    def read_by_user_id(self, user_id: str) -> object:
        try:
            customer = self.db.query(Customer).filter(Customer.user_id == user_id).first()
            return customer
        except Exception as exc:
            raise exc

    def read_customers_by_phone(self, phone: str) -> list[object]:
        try:
            customers = self.db.query(Customer).filter(Customer.phone == phone).all()
            return customers
        except Exception as exc:
            raise exc
