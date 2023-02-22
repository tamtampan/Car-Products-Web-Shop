"""Office Schema Module"""

from typing import Optional

from pydantic import UUID4, BaseModel


class OfficeSchema(BaseModel):
    """Office Schema"""

    office_id: UUID4
    name: str
    phone: str
    address: str
    city: str
    country: str
    postal_code: str
    territory: str

    class Config:
        """Config orm mode"""

        orm_mode = True


class OfficeSchemaIn(BaseModel):
    """Office Schema In"""

    name: str
    phone: str
    address: str
    city: str
    country: str
    postal_code: str
    territory: str

    class Config:
        """Config orm mode"""

        orm_mode = True


class OfficeSchemaUpdate(BaseModel):
    """Office Schema Update"""

    office_id: str
    name: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    city: Optional[str]
    country: Optional[str]
    postal_code: Optional[str]
    territory: Optional[str]

    class Config:
        """Config orm mode"""

        orm_mode = True
