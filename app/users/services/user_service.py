import codecs
import hashlib
from app.config import settings
from app.users.repositories.user_repository import UserRepository
from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidPassword


class UserService:

    @staticmethod
    def create_user(email, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(email, hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def create_superuser(email, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_superuser(email, hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def get_by_id(user_id: str):
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.read_by_id(user_id)

    @staticmethod
    def get_all():
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.read_all()

    @staticmethod
    def delete_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_by_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_active(user_id: str, active: bool):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_active(user_id, active)
            except Exception as e:
                raise e

    @staticmethod
    def login_user(email: str, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e
