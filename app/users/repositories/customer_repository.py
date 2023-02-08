from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import Customer


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name, surname, phone, address, city, country, postal_code, user_id):
        try:
            customer = Customer(name, surname, phone, address, city, country, postal_code, user_id)
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except IntegrityError as e:
            raise e

    def get_by_id(self, customer_id: str):
        customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
        return customer

    def get_all(self):
        customers = self.db.query(Customer).all()
        return customers

    def delete_by_id(self, customer_id: str):
        try:
            customer = self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
            self.db.delete(customer)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self):
        pass
