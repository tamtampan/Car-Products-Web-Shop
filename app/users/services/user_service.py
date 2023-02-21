import codecs
import hashlib

from app.config import settings
from app.users.repositories.user_repository import UserRepository
from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidPassword, UserPasswordLenError

from app.users.exceptions import UserNotFoundError
from sqlalchemy.exc import IntegrityError


class UserService:

    @staticmethod
    def create_user(email: str, password: str) -> object:
        try:
            if len(password) < 6:
                raise UserPasswordLenError()
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(email, hashed_password)
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def create_superuser(email: str, password: str) -> object:
        try:
            if len(password) < 6:
                raise UserPasswordLenError()
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_superuser(email, hashed_password)
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def login_user(email: str, password: str) -> object:
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.read_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for this user.", code=401)
                return user
        except Exception as e:
            raise e

    @staticmethod
    def read_by_id(user_id: str) -> object:
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.read_by_id(user_id)
                if user is None:
                    raise UserNotFoundError()
                return user
        except Exception as e:
            raise e

    @staticmethod
    def read_by_email(email: str) -> object:
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.read_by_email(email)
                if user is None:
                    raise UserNotFoundError()
                return user
        except Exception as e:
            raise e

    @staticmethod
    def read_all() -> list[object]:
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                users = user_repository.read_all()
                if len(users) == 0:
                    raise UserNotFoundError()
                return users
        except Exception as e:
            raise e

    @staticmethod
    def delete_by_id(user_id: str) -> bool:
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.delete_by_id(user_id)
                if user is None:
                    raise UserNotFoundError()
                return user
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    @staticmethod
    def update_active(user_id: str, active: bool) -> object:
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.update_active(user_id, active)
                if user is None:
                    raise UserNotFoundError()
                return user
        except Exception as e:
            raise e

    @staticmethod
    def update_password(email: str, password: str) -> object:
        try:
            with SessionLocal() as db:
                if len(password) < 6:
                    raise UserPasswordLenError()
                user_repository = UserRepository(db)
                user = user_repository.update_password(email, password)
                if user is None:
                    raise UserNotFoundError()
                return user
        except Exception as e:
            raise e
