from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.offices.models import Office
from app.offices.exceptions import *


class OfficeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name, phone, address, city, country, postal_code, territory):
        try:
            office = Office(name, phone, address, city, country, postal_code, territory)
            self.db.add(office)
            self.db.commit()
            self.db.refresh(office)
            return office
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_by_id(self, office_id: str):
        office = self.db.query(Office).filter(Office.office_id == office_id).first()
        if office is None:
            raise OfficeNotFoundException(f"Office with provided id - {office_id} not found.", 400)
        return office

    def read_all(self):
        offices = self.db.query(Office).all()
        return offices

    def delete_by_id(self, office_id: str):
        try:
            office = self.db.query(Office).filter(Office.office_id == office_id).first()
            if office is None:
                raise OfficeNotFoundException(f"Office with provided id - {office_id} not found.", 400)
            self.db.delete(office)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self, office_id: str, name: str = None, phone: str = None, address: str = None, city: str = None,
               country: str = None, postal_code: str = None, territory: str = None):
        try:
            office = self.db.query(Office).filter(Office.office_id == office_id).first()
            if office is None:
                raise OfficeNotFoundException(f"Office with provided id - {office_id} not found.", 400)
            if name is not None:
                office.name = name
            if phone is not None:
                office.phone = phone
            if address is not None:
                office.address = address
            if city is not None:
                office.city = city
            if country is not None:
                office.country = country
            if postal_code is not None:
                office.postal_code = postal_code
            if territory is not None:
                office.territory = territory
            self.db.add(office)
            self.db.commit()
            self.db.refresh(office)
            return office
        except Exception as e:
            raise e
