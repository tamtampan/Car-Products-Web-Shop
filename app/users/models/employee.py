from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Employee(Base):
    __tablename__ = "employee"
    employee_id = Column(String(100), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    job_title = Column(String(100), nullable=False)

    user_id = Column(String(100), ForeignKey("user.user_id"), nullable=False, unique=True)
    user = relationship("User", lazy='subquery')
    office_id = Column(String(100), ForeignKey("office.office_id"))
    office = relationship("Office", lazy='subquery')

    def __init__(self, name, surname, phone, job_title, user_id, office_id):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.job_title = job_title
        self.user_id = user_id
        self.office_id = office_id
