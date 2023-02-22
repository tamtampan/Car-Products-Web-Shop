"""Routes for Offices"""

from fastapi import APIRouter, Depends, Response

from app.offices.controller import OfficeController
from app.offices.schemas import OfficeSchema, OfficeSchemaIn, OfficeSchemaUpdate
from app.users.controller import JWTBearer

office_router = APIRouter(tags=["Offices"], prefix="/api/offices")


@office_router.post("/add-new-office", response_model=OfficeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_office(office: OfficeSchemaIn) -> object:
    """Create Office"""
    return OfficeController.create(
        office.name, office.phone, office.address, office.city, office.country, office.postal_code, office.territory
    )


@office_router.get("/id", response_model=OfficeSchema)
def get_office_by_id(office_id: str) -> object:
    """Get by id"""
    return OfficeController.read_by_id(office_id)


@office_router.get("/get-all-offices", response_model=list[OfficeSchema])
def get_all_offices() -> list[object]:
    """Get all"""
    return OfficeController.read_all()


@office_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_office_by_id(office_id: str) -> Response:
    """Delete by id"""
    return OfficeController.delete_by_id(office_id)


@office_router.put("/update/office", response_model=OfficeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_office(office: OfficeSchemaUpdate) -> object:
    """Update Office"""
    return OfficeController.update(
        office.office_id,
        office.name,
        office.phone,
        office.address,
        office.city,
        office.country,
        office.postal_code,
        office.territory,
    )


@office_router.get("/name", response_model=OfficeSchema)
def get_office_by_name(name: str) -> object:
    """Get by name"""
    return OfficeController.read_by_name(name)
