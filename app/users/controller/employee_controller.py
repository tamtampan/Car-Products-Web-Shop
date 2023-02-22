from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError

from app.offices.exceptions import OfficeNotFoundError
from app.offices.services import OfficeService
from app.users.exceptions import EmployeeNotFoundError, UserNotFoundError
from app.users.services import EmployeeService, UserService


class EmployeeController:
    """Employee Controller"""

    @staticmethod
    def create(name: str, surname: str, phone: str, job_title: str, user_id: str, office_id: str) -> object:
        """
        It creates an employee.

        :param name: str - the name of the employee
        :type name: str
        :param surname: str - the surname of the employee
        :type surname: str
        :param phone: str - phone number of employee
        :type phone: str
        :param job_title: str, user_id: str, office_id: str
        :type job_title: str
        :param user_id: str, office_id: str
        :type user_id: str
        :param office_id: str - the id of the office the employee is assigned to
        :type office_id: str
        :return: Employee object
        """

        try:
            UserService.read_by_id(user_id)
            OfficeService.read_by_id(office_id)
            employee = EmployeeService.create(name, surname, phone, job_title, user_id, office_id)
            return employee
        except IntegrityError:
            raise HTTPException(status_code=400, detail="User is already employee.")
        except UserNotFoundError:
            raise HTTPException(status_code=400, detail="You can not be employee if you are not user.")
        except OfficeNotFoundError:
            raise HTTPException(status_code=400, detail="No office with provided id found.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(employee_id: str) -> object:
        try:
            employee = EmployeeService.read_by_id(employee_id)
            return employee
        except EmployeeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all() -> list[object]:
        try:
            employee = EmployeeService.read_all()
            return employee
        except EmployeeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No employees in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(employee_id: str) -> Response:
        try:
            EmployeeService.delete_by_id(employee_id)
            return Response(status_code=200, content=f"Employee with id - {employee_id} deleted.")
        except EmployeeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update(
        employee_id: str, name: str = None, surname: str = None, phone: str = None, job_title: str = None
    ) -> object:
        try:
            employee = EmployeeService.update(employee_id, name, surname, phone, job_title)
            return employee
        except EmployeeNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
