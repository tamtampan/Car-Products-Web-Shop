from app.users.repositories.user_repository import UserRepository
from app.db.database import SessionLocal


class UserService:

    @staticmethod
    def create(email, password):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.create(email, password)
            except Exception as e:
                raise e

    @staticmethod
    def get_by_id(user_id: str):
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_by_id(user_id)

    @staticmethod
    def get_all():
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all()

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
                return user_repository.delete_by_id(user_id, active)
            except Exception as e:
                raise e
