from sqlalchemy.exc import IntegrityError
from app.users.services import EmployeeService, UserService
from app.offices.services import OfficeService
from fastapi import HTTPException, Response
from app.users.exceptions import EmployeeNotFoundException, UserNotFoundException
from app.offices.exceptions import OfficeNotFoundException


class EmployeeController:

    @staticmethod
    def create(name: str, surname: str, phone: str, job_title: str, user_id: str, office_id: str):
        try:
            UserService.read_by_id(user_id)
            OfficeService.read_by_id(office_id)
            employee = EmployeeService.create(name, surname, phone, job_title, user_id, office_id)
            return employee
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User is already employee.")
        except UserNotFoundException:
            raise HTTPException(status_code=400, detail=f"You can not be employee if you are not user.")
        except OfficeNotFoundException:
            raise HTTPException(status_code=400, detail=f"No office with provided id found.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(employee_id: str):
        try:
            employee = EmployeeService.read_by_id(employee_id)
            return employee
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all():
        try:
            employee = EmployeeService.read_all()
            return employee
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(employee_id: str):
        try:
            EmployeeService.delete_by_id(employee_id)
            return Response(status_code=200, content=f"Employee with id - {employee_id} deleted.")
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(employee_id: str, name: str = None, surname: str = None, phone: str = None, job_title: str = None):
        try:
            employee = EmployeeService.update(employee_id, name, surname, phone, job_title)
            return employee
        except EmployeeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
