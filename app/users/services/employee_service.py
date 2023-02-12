from app.users.repositories.employee_repository import EmployeeRepository
from app.db.database import SessionLocal


class EmployeeService:

    @staticmethod
    def create(name: str, surname: str, phone: str, job_title: str, user_id: str):
        with SessionLocal() as db:
            try:
                employee_repository = EmployeeRepository(db)
                return employee_repository.create(name, surname, phone, job_title, user_id)
            except Exception as e:
                raise e

    @staticmethod
    def read_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_by_id(employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.read_all()
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(employee_id: str):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.delete_by_id(employee_id)
        except Exception as e:
            raise e

    @staticmethod
    def update(employee_id: str, name: str = None, surname: str = None, phone: str = None, job_title: str = None):
        try:
            with SessionLocal() as db:
                employee_repository = EmployeeRepository(db)
                return employee_repository.update(employee_id, name, surname, phone, job_title)
        except Exception as e:
            raise e
