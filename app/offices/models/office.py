from uuid import uuid4
from sqlalchemy import Column, String
from app.db import Base


class Office(Base):
    __tablename__ = "offices"
    office_id = Column(String(50), primary_key=True, default=uuid4)
    office_name = Column(String(50), nullable=False)
    office_phone = Column(String(50), nullable=False)
    office_address = Column(String(100), nullable=False)
    office_city = Column(String(50), nullable=False)
    office_state = Column(String(50), nullable=False)
    office_postal_code = Column(String(50), nullable=False)
    office_territory = Column(String(50))

    def __init__(self, office_name, office_phone, office_address, office_city, office_state, office_postal_code,
                 office_territory):
        self.office_name = office_name
        self.office_phone = office_phone
        self.office_address = office_address
        self.office_city = office_city
        self.office_state = office_state
        self.office_postal_code = office_postal_code
        self.office_territory = office_territory
