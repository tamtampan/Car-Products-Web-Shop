from typing import Optional

from pydantic import UUID4, BaseModel

from app.offices.schemas import OfficeSchema
from app.users.schemas import UserSchema


class EmployeeSchema(BaseModel):
    """Employee Schema"""

    employee_id: UUID4
    name: str
    surname: str
    phone: str
    job_title: str
    user_id: str
    user: UserSchema
    office_id: str
    office: OfficeSchema

    class Config:
        orm_mode = True


class EmployeeSchemaIn(BaseModel):
    """Employee Schema In"""

    name: str
    surname: str
    phone: str
    job_title: str
    user_id: str
    office_id: str

    class Config:
        orm_mode = True


class EmployeeSchemaUpdate(BaseModel):
    """Employee Schema Update"""

    employee_id: str
    name: Optional[str]
    surname: Optional[str]
    phone: Optional[str]
    job_title: Optional[str]
