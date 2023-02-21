import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.offices.repositories import OfficeRepository


# ----- copy:
# pytest app/offices/tests/unittests/test_offices.py

def create_offices_for_methods():
    with TestingSessionLocal() as db:
        office_repository = OfficeRepository(db)
        office_repository.create("Office1", "011 262 555", "Address", "City", "Country", "Postal code", "Territory")
        office_repository.create("Office2", "011 262 555", "Address", "City", "Country", "Postal code", "Territory")
        office_repository.create("Office3", "011 262 555", "Address", "City", "Country", "Postal code", "Territory")
        office_repository.create("Office4", "011 262 555", "Address", "City", "Country", "Postal code", "Territory")


class TestOfficeRepo(TestClass):

    def test_create_office(self):
        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            office = office_repository.create("Office", "011 262 555", "Address", "City", "Country", "Postal code",
                                              "Territory")
            assert office.name == "Office"
            assert office.phone == "011 262 555"
            assert office.address == "Address"
            assert office.city == "City"
            assert office.country == "Country"
            assert office.postal_code == "Postal code"
            assert office.territory == "Territory"

    def test_create_office_error(self):
        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            office = office_repository.create("Office", "011 262 555", "Address", "City", "Country", "Postal code",
                                              "Territory")
            with pytest.raises(IntegrityError):
                office_repository.create("Office", "011 262 555", "Address", "City", "Country", "Postal code",
                                         "Territory")

    def test_get_by_id(self):
        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            office = office_repository.create("Office", "011 262 555", "Address", "City", "Country", "Postal code",
                                              "Territory")
            office2 = office_repository.read_by_id(office.office_id)
            assert office.office_id == office2.office_id
            assert office.name == office2.name
            assert office.phone == office2.phone
            assert office.address == office2.address
            assert office.city == office2.city
            assert office.country == office2.country
            assert office.postal_code == office2.postal_code
            assert office.territory == office2.territory

    def test_get_all_users(self):
        create_offices_for_methods()
        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            all_offices = office_repository.read_all()
            assert len(all_offices) == 4

    def test_get_all_offices_error(self):
        create_offices_for_methods()
        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            all_offices = office_repository.read_all()
            assert not len(all_offices) != 4

    def test_delete_office_by_id(self):
        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            office = office_repository.create("Office", "011 262 555", "Address", "City", "Country", "Postal code",
                                              "Territory")
            assert office_repository.delete_by_id(office.office_id) is True

    # def test_delete_office_by_id_error(self): # WTF
    #     with TestingSessionLocal() as db:
    #         office_repository = OfficeRepository(db)
    #         office = office_repository.create("Office", "011 262 555", "Address", "City", "Country", "Postal code",
    #                                           "Territory")
    #         assert office_repository.delete_by_id(office.office_id) is not False

    def test_update_office(self):
        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            office = office_repository.create("Office", "011 262 555", "Address", "City", "Country", "Postal code",
                                              "Territory")
            office1 = office_repository.update(office.office_id, name="New Office")
            assert office1.name == "New Office"

    # def test_update_user_is_active_error(self):
    #     with TestingSessionLocal() as db:
    #         office_repository = OfficeRepository(db)
    #         office = office_repository.create_user("velja@gmail.com", "1234")
    #         office = office_repository.update_active(office.user_id, False)
    #         assert office.active is not True
    #
    # def test_read_user_by_email(self):
    #     with TestingSessionLocal() as db:
    #         office_repository = OfficeRepository(db)
    #         office = office_repository.create_user("velja@gmail.com", "1234")
    #         assert office.email == "velja@gmail.com"
    #
    # def test_read_user_by_email_error(self):
    #     with TestingSessionLocal() as db:
    #         office_repository = OfficeRepository(db)
    #         office = office_repository.create_user("velja@gmail.com", "1234")
    #         assert not office.email != "velja@gmail.com"
