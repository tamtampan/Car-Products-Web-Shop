from fastapi import APIRouter, Depends
from app.users.controller import UserController
from app.users.schemas import *
from app.users.controller.user_authentication_controller import JWTBearer

user_router = APIRouter(tags=["Users"], prefix="/api/users")

# dependencies=[Depends(JWTBearer("super_user"))]


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.email, user.password)


@user_router.post("/add-new-superuser", response_model=UserSchema)
def create_superuser(user: UserSchemaIn):
    return UserController.create_superuser(user.email, user.password)


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.get("/id", response_model=UserSchema)
def get_by_id(user_id: str):
    return UserController.get_by_id(user_id)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all()


@user_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_by_id(user_id: str):
    return UserController.delete_by_id(user_id)


@user_router.put("/update/active", response_model=UserSchema)
def update_user(user_id: str, active: bool):
    return UserController.update_active(user_id, active)
