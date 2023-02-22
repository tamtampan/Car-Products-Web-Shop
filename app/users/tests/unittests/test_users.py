import pytest
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.users.repositories import UserRepository

# ----- copy:
# pytest app/users/tests/unittests/test_users.py

# if circular import error - make sure app/users/schemas/__init__.py has the right order of imports


def create_users_for_methods():
    with TestingSessionLocal() as db:
        user_repository = UserRepository(db)
        user_repository.create_user("tamarapantic1@gmail.com", "1234567")
        user_repository.create_user("tamarapantic2@gmail.com", "1234567")
        user_repository.create_user("tamarapantic3@gmail.com", "1234567")
        user_repository.create_user("tamarapantic4@gmail.com", "1234567")


class TestUserRepo(TestClass):
    def test_create_user(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user(email="tamtam@gmail.com", password="1234567")
            assert user.email == "tamtam@gmail.com"
            assert user.superuser is False
            assert user.active is True

    def test_create_user_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("tamtam@gmail.com", "1234567")
            assert user.active is not False
            with pytest.raises(IntegrityError):
                user_repository.create_user("tamtam@gmail.com", "1234567")

    def test_create_superuser(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            superuser = user_repository.create_superuser("daki@gmail.com", "1234567")
            assert superuser.email == "daki@gmail.com"
            assert superuser.superuser is True

    def test_create_superuser_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            superuser = user_repository.create_superuser("tamtam@gmail.com", "1234567")
            assert superuser.superuser is not False
            with pytest.raises(IntegrityError):
                user_repository.create_superuser("tamtam@gmail.com", "1234567")

    def test_get_by_id(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("tamtam@gmail.com", "1234567")
            user1 = user_repository.read_by_id(user.user_id)
            assert user.user_id == user1.user_id
            assert user.email == user1.email
            assert user.password == user1.password

    def test_get_all_users(self):
        create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.read_all()
            assert len(all_users) == 4

    def test_get_all_users_error(self):
        create_users_for_methods()
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            all_users = user_repository.read_all()
            assert not len(all_users) != 4

    def test_delete_user_by_id(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("tamtam@gmail.com", "1234567")
            assert user_repository.delete_by_id(user.user_id) is True

    def test_delete_user_by_id_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("tamtam@gmail.com", "1234567")
            assert user_repository.delete_by_id(user.user_id) is not False

    def test_update_user_active(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("tamtam@gmail.com", "1234567")
            user = user_repository.update_active(user.user_id, False)
            assert user.active is False

    def test_update_user_is_active_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("tamtam@gmail.com", "1234567")
            user = user_repository.update_active(user.user_id, False)
            assert user.active is not True

    def test_read_user_by_email(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("tamtam@gmail.com", "1234567")
            assert user.email == "tamtam@gmail.com"

    def test_read_user_by_email_error(self):
        with TestingSessionLocal() as db:
            user_repository = UserRepository(db)
            user = user_repository.create_user("tamtam@gmail.com", "1234567")
            assert not user.email != "tamtam@gmail.com"
