from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, email, password):
        try:
            user = User(email, password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def get_by_id(self, user_id: str):
        user = self.db.query(User).filter(User.user_id == user_id).first()
        return user

    def get_all(self):
        users = self.db.query(User).all()
        return users

    def delete_by_id(self, user_id: str):
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_active(self, user_id: str, active: bool):
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            user.active = active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e
