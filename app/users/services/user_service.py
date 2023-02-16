import codecs
import hashlib

from app.config import settings
from app.users.repositories.user_repository import UserRepository
from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidPassword


class UserService:

    @staticmethod
    def create_user(email, password: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(email, hashed_password)
        except Exception as e:
            raise e

    @staticmethod
    def create_superuser(email, password: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_superuser(email, hashed_password)
        except Exception as e:
            raise e

    @staticmethod
    def login_user(email: str, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for this user.", code=401)
                return user
            except Exception as e:
                raise e

    @staticmethod
    def read_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.read_by_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_by_email(email: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.read_by_email(email)
        except Exception as e:
            raise e

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.read_all()
        except Exception as e:
            raise e

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


    # @staticmethod
    # def read_faculty_by_acronym(acronym: str) -> FacultyExceptionCode or Faculty:
    #     try:
    #         with SessionLocal() as db:
    #             repository = FacultyRepository(db)
    #             return repository.read_faculty_by_acronym(acronym)
    #     except Exception as e:
    #         raise e
    #
    # @staticmethod
    # def read_faculty_by_city(city: str):
    #     try:
    #         with SessionLocal() as db:
    #             repository = FacultyRepository(db)
    #             return repository.read_faculty_by_city(city)
    #     except Exception as e:
    #         raise e
    #
    # @staticmethod
    # def read_faculty_by_name(name: str):
    #     try:
    #         with SessionLocal() as db:
    #             repository = FacultyRepository(db)
    #             return repository.read_faculty_by_name(name)
    #     except Exception as e:
    #         raise e
    #
    # @staticmethod
    # def read_faculty_by_name_or_city(namecity: str):
    #     try:
    #         with SessionLocal() as db:
    #             repository = FacultyRepository(db)
    #             return repository.read_faculty_by_name_or_city(namecity)
    #     except Exception as e:
    #         raise e
