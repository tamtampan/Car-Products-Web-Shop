from sqlalchemy.exc import IntegrityError
from app.users.services import UserService, signJWT
from fastapi import HTTPException, Response
from app.users.exceptions import UserInvalidPassword, UserNotFoundError, UserPasswordLenError
from typing import Dict


class UserController:

    @staticmethod
    def create_user(email, password: str) -> object:
        try:
            user = UserService.create_user(email, password)
            return user
        except UserPasswordLenError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_superuser(email, password) -> object:
        try:
            user = UserService.create_superuser(email, password)
            return user
        except UserPasswordLenError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email, password) -> Dict[str, str]:
        try:
            user = UserService.login_user(email, password)
            if user.superuser:
                return signJWT(user.user_id, "super_user")
            return signJWT(user.user_id, "classic_user")
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(user_id: str) -> object:
        try:
            user = UserService.read_by_id(user_id)
            return user
        except UserNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_email(email: str) -> object:
        try:
            user = UserService.read_by_email(email)
            return user
        except UserNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all() -> list[object]:
        try:
            users = UserService.read_all()
            return users
        except UserNotFoundError as e:
            raise HTTPException(status_code=e.code, detail="No users in system.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(user_id: str) -> Response:
        try:
            UserService.delete_by_id(user_id)
            return Response(status_code=200, content=f"User with id - {user_id} deleted.")
        except UserNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail="Can not delete user before deleting customer (or employee).")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_active(user_id: str, active: bool) -> object:
        try:
            user = UserService.update_active(user_id, active)
            return user
        except UserNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_password(email: str, password: str) -> object:
        try:
            user = UserService.update_password(email, password)
            return user
        except UserPasswordLenError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotFoundError as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
