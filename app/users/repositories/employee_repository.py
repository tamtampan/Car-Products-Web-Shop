from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import Employee
from app.users.exceptions import EmployeeNotFoundException


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
        except Exception as e:
            raise e

    def read_by_id(self, employee_id: str):
        employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
        if employee is None:
            raise EmployeeNotFoundException(f"Employee with provided id: {employee_id} not found.", 400)
        return employee

    def read_all(self):
        employees = self.db.query(Employee).all()
        return employees

    def delete_by_id(self, employee_id: str):
        try:
            employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
            if employee is None:
                raise EmployeeNotFoundException(f"Employee with provided id: {employee_id} not found.", 400)
            self.db.delete(employee)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(self, employee_id: str, name: str = None, surname: str = None, phone: str = None, job_title: str = None):
        try:
            employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
            if employee is None:
                raise EmployeeNotFoundException(f"Employee with provided id: {employee_id} not found.", 400)
            if name is not None:
                employee.name = name
            if surname is not None:
                employee.surname = surname
            if phone is not None:
                employee.phone = phone
            if job_title is not None:
                employee.address = job_title
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except Exception as e:
            raise e
