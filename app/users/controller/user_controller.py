from sqlalchemy.exc import IntegrityError
from app.users.services import UserService, signJWT
from fastapi import HTTPException, Response
from app.users.exceptions import UserInvalidPassword


class UserController:

    @staticmethod
    def create_user(email, password):
        try:
            user = UserService.create_user(email, password)
            return user
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_superuser(email, password):
        try:
            user = UserService.create_superuser(email, password)
            return user
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email, password):
        try:
            user = UserService.login_user(email, password)
            if user.is_superuser:
                return signJWT(user.id, "super_user")
            return signJWT(user.id, "classic_user")
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_by_id(user_id: str):
        user = UserService.get_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=400, detail=f"User with provided id {user_id} does not exists.")

    @staticmethod
    def get_all():
        users = UserService.get_all()
        return users

    @staticmethod
    def delete_by_id(user_id: str):
        try:
            UserService.delete_by_id(user_id)
            return Response(content=f"User with id - {user_id} is deleted.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_active(user_id: str, active: bool):
        try:
            user = UserService.update_active(user_id, active)
            return user
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
