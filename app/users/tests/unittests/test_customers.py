from app.tests import TestClass, TestingSessionLocal
from app.users.repositories import CustomerRepository


# ----- copy:
# pytest app/users/tests/unittests/test_customers.py


class TestCustomerRepository(TestClass):
    def test_create_customer(self):
        with TestingSessionLocal() as db:
            customer_repository = CustomerRepository(db)
            customer = customer_repository.create(
                "Name", "Surname", "0654488989", "Address", "City", "Country", "11000", "xxx"
            )
            assert customer.name == "Name"
            assert customer.surname == "Surname"
