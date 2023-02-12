from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import User
from app.users.exceptions import UserNotFoundException


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email, password):
        try:
            user = User(email, password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def create_superuser(self, email, password):
        try:
            user = User(email=email, password=password, superuser=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_by_id(self, user_id: str):
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user is None:
            raise UserNotFoundException(f"User with provided id: {user_id} not found.", 400)
        return user

    def read_by_email(self, email: str):
        user = self.db.query(User).filter(User.email == email).first()
        if user is None:
            raise UserNotFoundException(f"User with provided email: {email} not found.", 400)
        return user

    def read_all(self):
        users = self.db.query(User).all()
        return users

    def delete_by_id(self, user_id: str):
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            if user is None:
                raise UserNotFoundException(f"User with provided id: {user_id} not found.", 400)
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_active(self, user_id: str, active: bool):
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            if user is None:
                raise UserNotFoundException(f"User with provided id: {user_id} not found.", 400)
            user.active = active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e
