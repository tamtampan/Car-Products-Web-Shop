from uuid import uuid4
from sqlalchemy import Column, String, Boolean
from app.db import Base


class User(Base):
    __tablename__ = "user"
    user_id = Column(String(50), primary_key=True, default=uuid4)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(50))
    active = Column(Boolean, default=True)
    superuser = Column(Boolean, default=False)

    def __init__(self, email, password, active=True, superuser=False):
        self.email = email
        self.password = password
        self.active = active
        self.superuser = superuser
