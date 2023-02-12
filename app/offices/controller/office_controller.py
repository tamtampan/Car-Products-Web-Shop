from app.offices.services import OfficeService
from fastapi import HTTPException, Response, status
# from app.offices.exceptions import *


class OfficeController:

    @staticmethod
    def create(name, phone, address, city, country, postal_code, territory):
        try:
            office = OfficeService.create(name, phone, address, city, country, postal_code, territory)
            return office
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_by_id(office_id: str):
        office = OfficeService.read_by_id(office_id)
        if office:
            return office
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Office with provided id {office_id} does not exist")

    @staticmethod
    def get_all():
        office = OfficeService.read_all()
        return office

    @staticmethod
    def delete_by_id(office_id: str):
        try:
            OfficeService.delete_by_id(office_id)
            return Response(content=f"Office with id - {office_id} is deleted")
        # except EmployeeNotFoundException as e:
        #     raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update(office_id: str, name: str = None, phone: str = None, address: str = None, city: str = None,
               country: str = None, postal_code: str = None, territory: str = None):
        try:
            office = OfficeService.update(office_id, name, phone, address, city, country, postal_code, territory)
            return office
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # @staticmethod
    # def get_employees_by_characters(characters: str):
    #     employees = EmployeeServices.get_employees_by_characters(characters)
    #     if employees:
    #         return employees
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
    #                         detail=f"Employee with provided characters {characters} does not exist")
    #
    # @staticmethod
    # def get_employees_by_employee_type_id(employee_type_id: str):
    #     employees = EmployeeServices.get_employees_by_employee_type_id(employee_type_id)
    #     if employees:
    #         return employees
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
    #                         detail=f"Employee with provided employee type id {employee_type_id} does not exist")
