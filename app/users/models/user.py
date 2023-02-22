from uuid import uuid4

from sqlalchemy import Boolean, Column, String

from app.db import Base


class User(Base):
    """User Model"""

    __tablename__ = "user"
    user_id = Column(String(100), primary_key=True, default=uuid4)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    superuser = Column(Boolean, default=False)

    def __init__(self, email, password, active=True, superuser=False):
        self.email = email
        self.password = password
        self.active = active
        self.superuser = superuser
