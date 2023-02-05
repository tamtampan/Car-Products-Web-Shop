from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Employee(Base):
    __tablename__ = "employee"
    employee_id = Column(String(50), primary_key=True, default=uuid4)
    employee_name = Column(String(50), nullable=False)
    employee_surname = Column(String(50), nullable=False)
    employee_phone = Column(String(50), nullable=False)
    employee_job_title = Column(String(100), nullable=False)

    user_id = Column(String(50), ForeignKey("user.user_id"), nullable=False)
    user = relationship("User", lazy='subquery')

    def __init__(self, employee_name, employee_surname, employee_phone, employee_job_title, user_id):
        self.employee_name = employee_name
        self.employee_surname = employee_surname
        self.employee_phone = employee_phone
        self.employee_job_title = employee_job_title
        self.user_id = user_id
