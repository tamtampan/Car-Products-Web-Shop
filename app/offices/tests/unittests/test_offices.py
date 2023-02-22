"""Test Office Repository"""

import pytest
from sqlalchemy.exc import IntegrityError

from app.offices.repositories import OfficeRepository
from app.tests import TestClass, TestingSessionLocal

# ----- copy:
# pytest app/offices/tests/unittests/test_offices.py

# if circular import error - make sure app/users/schemas/__init__.py has the right order of imports


def create_offices_for_methods():
    """Create offices for methods"""

    with TestingSessionLocal() as db:
        office_repository = OfficeRepository(db)
        office_repository.create("Office1", "011 262 555", "Address", "City", "Country", "Postal code", "Territory")
        office_repository.create("Office2", "011 262 555", "Address", "City", "Country", "Postal code", "Territory")
        office_repository.create("Office3", "011 262 555", "Address", "City", "Country", "Postal code", "Territory")
        office_repository.create("Office4", "011 262 555", "Address", "City", "Country", "Postal code", "Territory")


class TestOfficeRepo(TestClass):
    """Test Office Repository"""

    def test_create_office(self):
        """Create test"""

        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            office = office_repository.create(
                "Office", "011 262 555", "Address", "City", "Country", "Postal code", "Territory"
            )
            assert office.name == "Office"
            assert office.phone == "011 262 555"
            assert office.address == "Address"
            assert office.city == "City"
            assert office.country == "Country"
            assert office.postal_code == "Postal code"
            assert office.territory == "Territory"

    def test_create_office_error(self):
        """Create with error test"""

        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            office = office_repository.create(
                "Office", "011 262 555", "Address", "City", "Country", "Postal code", "Territory"
            )
            with pytest.raises(IntegrityError):
                office_repository.create(
                    "Office", "011 262 555", "Address", "City", "Country", "Postal code", "Territory"
                )

    def test_get_by_id(self):
        """Get by id test"""

        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            office = office_repository.create(
                "Office", "011 262 555", "Address", "City", "Country", "Postal code", "Territory"
            )
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
        """Get all test"""

        create_offices_for_methods()
        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            all_offices = office_repository.read_all()
            assert len(all_offices) == 4

    def test_get_all_offices_error(self):
        """Get all error test"""

        create_offices_for_methods()
        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            all_offices = office_repository.read_all()
            assert not len(all_offices) != 4

    def test_delete_office_by_id(self):
        """Delete test"""

        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            office = office_repository.create(
                "Office", "011 262 555", "Address", "City", "Country", "Postal code", "Territory"
            )
            assert office_repository.delete_by_id(office.office_id) is True

    def test_update_office(self):
        """Update test"""

        with TestingSessionLocal() as db:
            office_repository = OfficeRepository(db)
            office = office_repository.create(
                "Office", "011 262 555", "Address", "City", "Country", "Postal code", "Territory"
            )
            office1 = office_repository.update(office.office_id, name="New Office")
            assert office1.name == "New Office"
