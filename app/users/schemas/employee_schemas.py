from pydantic import BaseModel
from pydantic import UUID4

from app.offices.schemas import OfficeSchema
from app.users.schemas import UserSchema


class EmployeeSchema(BaseModel):
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
    name: str
    surname: str
    phone: str
    job_title: str
    user_id: str
    office_id: str

    class Config:
        orm_mode = True
