from fastapi import APIRouter
from app.offices.controller import OfficeController
from app.offices.schemas import *
from fastapi import Response

office_router = APIRouter(tags=["Offices"], prefix="/api/offices")


@office_router.post("/add-new-office", response_model=OfficeSchema)
def create_office(office: OfficeSchemaIn) -> object:
    return OfficeController.create(office.name, office.phone, office.address, office.city, office.country,
                                   office.postal_code, office.territory)


@office_router.get("/id", response_model=OfficeSchema)
def get_office_by_id(office_id: str) -> object:
    return OfficeController.read_by_id(office_id)


@office_router.get("/get-all-offices", response_model=list[OfficeSchema])
def get_all_offices() -> list[object]:
    return OfficeController.read_all()


@office_router.delete("/")
def delete_office_by_id(office_id: str) -> Response:
    return OfficeController.delete_by_id(office_id)


@office_router.put("/update/office", response_model=OfficeSchema)
def update_office(office_id: str, name: str = None, phone: str = None, address: str = None, city: str = None,
                  country: str = None, postal_code: str = None, territory: str = None) -> object:
    return OfficeController.update(office_id, name, phone, address, city, country, postal_code, territory)


@office_router.get("/name", response_model=OfficeSchema)
def get_office_by_name(name: str) -> object:
    return OfficeController.read_by_name(name)
