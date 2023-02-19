from sqlalchemy.orm import Session
from app.users.models import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email, password) -> object:
        try:
            user = User(email, password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def create_superuser(self, email, password) -> object:
        try:
            user = User(email=email, password=password, superuser=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def read_by_id(self, user_id: str) -> object:
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            return user
        except Exception as e:
            raise e

    def read_by_email(self, email: str) -> object:
        try:
            user = self.db.query(User).filter(User.email == email).first()
            return user
        except Exception as e:
            raise e

    def read_all(self) -> list[object]:
        try:
            users = self.db.query(User).all()
            return users
        except Exception as e:
            raise e

    def delete_by_id(self, user_id: str) -> bool or None:
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            if user is None:
                return None
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_active(self, user_id: str, active: bool) -> object:
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            if user is None:
                return None
            user.active = active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def update_password(self, email: str, password: str) -> object:
        try:
            user = self.db.query(User).filter(User.email == email).first()
            if user is None:
                return None
            user.password = password
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e
