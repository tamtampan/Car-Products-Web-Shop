"""User repositories module"""
from typing import Type

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.users.models import User


class UserRepository:
    """User Repository class"""

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email, password) -> User:
        """create_user function"""
        try:
            user = User(email, password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as exc:
            raise exc

    def create_superuser(self, email, password) -> User:
        try:
            user = User(email=email, password=password, superuser=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as exc:
            raise exc

    def read_by_id(self, user_id: str) -> Type[User] | None:
        """read_by_id function"""
        user = self.db.query(User).filter(User.user_id == user_id).first()
        return user

    def read_by_email(self, email: str) -> Type[User] | None:
        """read_by_email function"""
        user = self.db.query(User).filter(User.email == email).first()
        return user

    def read_all(self) -> list[Type[User]]:
        users = self.db.query(User).all()
        return users

    def delete_by_id(self, user_id: str) -> bool or None:
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            if user is None:
                return None
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as exc:
            raise exc

    def delete_by_email(self, email: str) -> bool or None:
        try:
            user = self.db.query(User).filter(User.email == email).first()
            if user is None:
                return None
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as exc:
            raise exc

    def update_active(self, user_id: str, active: bool) -> Type[User] | None:
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            if user is None:
                return None
            user.active = active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as exc:
            raise exc

    def update_password(self, email: str, password: str) -> Type[User] | None:
        try:
            user = self.db.query(User).filter(User.email == email).first()
            if user is None:
                return None
            user.password = password
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as exc:
            raise exc
