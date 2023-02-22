from sqlalchemy.orm import Session

from app.users.models import Employee


class EmployeeRepository:
    """Employee Repository"""

    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, surname: str, phone: str, job_title: str, user_id: str, office_id: str) -> object:
        try:
            employee = Employee(name, surname, phone, job_title, user_id, office_id)
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except Exception as e:
            raise e

    def read_by_id(self, employee_id: str) -> object:
        try:
            employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
            return employee
        except Exception as e:
            raise e

    def read_all(self) -> list[object]:
        try:
            employees = self.db.query(Employee).all()
            return employees
        except Exception as e:
            raise e

    def delete_by_id(self, employee_id: str) -> bool or None:
        try:
            employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
            if employee is None:
                return None
            self.db.delete(employee)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update(
        self, employee_id: str, name: str = None, surname: str = None, phone: str = None, job_title: str = None
    ) -> object:
        try:
            employee = self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
            if employee is None:
                return None
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
