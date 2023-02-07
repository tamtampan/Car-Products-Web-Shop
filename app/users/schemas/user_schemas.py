from pydantic import BaseModel
from pydantic import UUID4, EmailStr


class UserSchema(BaseModel):
    user_id: UUID4
    email: str
    password: str
    active: bool
    superuser: bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
