from sqlalchemy.exc import IntegrityError
from app.users.services import UserService, signJWT
from fastapi import HTTPException, Response
from app.users.exceptions import UserInvalidPassword, UserNotFoundException


class UserController:

    @staticmethod
    def create_user(email, password: str):
        try:
            user = UserService.create_user(email, password)
            return user
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_superuser(email, password):
        try:
            user = UserService.create_superuser(email, password)
            return user
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email, password):
        try:
            user = UserService.login_user(email, password)
            if user.superuser:
                return signJWT(user.user_id, "super_user")
            return signJWT(user.user_id, "classic_user")
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_id(user_id: str):
        try:
            user = UserService.read_by_id(user_id)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_by_email(email: str):
        try:
            user = UserService.read_by_email(email)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def read_all():  # da li se ovde raisuje exception ako je len od liste = 0
        try:
            users = UserService.read_all()
            return users
        except Exception as e:  # ------------------------------------JE L MOZE OVAKO?
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_by_id(user_id: str):
        try:
            UserService.delete_by_id(user_id)
            return Response(status_code=200, content=f"User with id - {user_id} deleted.")
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))  # referencijalni integritet pazi kad brises usera

    @staticmethod
    def update_active(user_id: str, active: bool):
        try:
            user = UserService.update_active(user_id, active)
            return user
        except UserNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# ----------------------------------------------------------------------------------
# from app.faculties.exceptions import FacultyExceptionCode, FacultyNotFoundException


#
#     @staticmethod
#     def get_faculty_by_acronym(faculty_acronym: str):
#         try:
#             faculty = FacultyService.read_faculty_by_acronym(faculty_acronym)
#             return faculty
#         except FacultyNotFoundException as e:
#             print(e)
#             raise HTTPException(status_code=e.code, detail=e.message)
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=str(e))
#
#     @staticmethod
#     def get_faculty_by_city(city: str):
#         try:
#             faculty = FacultyService.read_faculty_by_city(city)
#             return faculty
#         except FacultyNotFoundException as e:
#             print(e)
#             raise HTTPException(status_code=e.code, detail=e.message)
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=str(e))
#
#     @staticmethod
#     def get_faculty_by_name(name: str):
#         try:
#             faculty = FacultyService.read_faculty_by_name(name)
#             return faculty
#         except FacultyNotFoundException as e:
#             print(e)
#             raise HTTPException(status_code=e.code, detail=e.message)
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=str(e))
#
#     @staticmethod
#     def get_faculty_by_name_or_city(namecity: str):
#         try:
#             faculty = FacultyService.read_faculty_by_name_or_city(namecity)
#             return faculty
#         except FacultyNotFoundException as e:
#             print(e)
#             raise HTTPException(status_code=e.code, detail=e.message)
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=str(e))
