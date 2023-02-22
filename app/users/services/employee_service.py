from sqlalchemy.exc import IntegrityError

from app.db.database import SessionLocal
from app.users.exceptions import EmployeeNotFoundError
from app.users.repositories.employee_repository import EmployeeRepository


class EmployeeService:
    """Employee Service"""

    @staticmethod
    def create(name: str, surname: str, phone: str, job_title: str, user_id: str, office_id: str) -> object:
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.create(name, surname, phone, job_title, user_id, office_id)
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(employee_id: str) -> object:
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                employee = employee_repository.read_by_id(employee_id)
                if employee is None:
                    raise EmployeeNotFoundError()
                return employee
        except Exception as e:
            raise e

    @staticmethod
    def read_all() -> list[object]:
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                employees = employee_repository.read_all()
                if len(employees) == 0:
                    raise EmployeeNotFoundError()
                return employees
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(employee_id: str) -> bool:
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                employee = employee_repository.delete_by_id(employee_id)
                if employee is None:
                    raise EmployeeNotFoundError()
                return employee
        except Exception as e:
            raise e

    @staticmethod
    def update(
        employee_id: str, name: str = None, surname: str = None, phone: str = None, job_title: str = None
    ) -> object:
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                employee = employee_repository.update(employee_id, name, surname, phone, job_title)
                if employee is None:
                    raise EmployeeNotFoundError()
                return employee
        except Exception as e:
            raise e
