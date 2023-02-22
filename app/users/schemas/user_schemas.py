from pydantic import UUID4, BaseModel, EmailStr


class UserSchema(BaseModel):
    """User Schema"""

    user_id: UUID4
    email: str
    password: str
    active: bool
    superuser: bool

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    """User Schema In"""

    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserSchemaUpdateActive(BaseModel):
    """User Schema Update Active"""

    user_id: str
    active: bool

    class Config:
        orm_mode = True


class UserSchemaUpdatePassword(BaseModel):
    """User Schema Update Password"""

    email: EmailStr
    password: str

    class Config:
        orm_mode = True
