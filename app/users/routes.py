from fastapi import APIRouter

from app.users.controller import UserController
from app.users.schemas import *

user_router = APIRouter(tags=["users"], prefix="/api/users")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create(user.email, user.password)


@user_router.get("/id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_by_id(user_id)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all()


@user_router.delete("/")
def delete_user_by_id(user_id: str):
    return UserController.delete_by_id(user_id)


@user_router.put("/update/active", response_model=UserSchema)
def update_user(user_id: str, active: bool):
    return UserController.update_active(user_id, active)


student_router = APIRouter(tags=["students"], prefix="/api/students")

