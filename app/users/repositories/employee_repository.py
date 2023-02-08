from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import Employee


class EmployeeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name, surname, phone, job_title, user_id):
        try:
            employee = Employee(name, surname, phone, job_title, user_id)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except IntegrityError as e:
            raise e

    def get_by_id(self, employee_id: str):
        employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
        return employee

    def get_all(self):
        employees = self.db.query(Employee).all()
        return employees

    def delete_by_id(self, employee_id: str):
        try:
            employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
            self.db.delete(employee)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self):
        pass
