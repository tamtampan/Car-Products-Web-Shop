# import uvicorn
# from fastapi import FastAPI
#
# from app.db.database import engine, Base
# from app.users.routes import user_router, student_router
#
#
# Base.metadata.create_all(bind=engine)
#
#
# def init_app():
#     app = FastAPI()
#     app.include_router(user_router)
#     app.include_router(student_router)
#     return app
#
#
# app = init_app()
#
#
# @app.get("/")
# def root():
#     return {"cao": "cao"}
#
#
# if __name__ == "__main__":
#     uvicorn.run(app)




# import uvicorn
# from fastapi import FastAPI
# from starlette.responses import RedirectResponse
#
# from app.db.database import engine, Base
# from app.users.routes import user_router, student_router, employee_router, employee_type_router
# from app.faculties.routes import faculty_router
# from app.users.routes import user_router, student_router
#
# from app.courses.routes import course_router
# from app.study_programmes import study_programme_router, year_of_study_router
# from app.school_years.routes import school_year_router
#
#
# Base.metadata.create_all(bind=engine)
#
#
# def init_app():
#     app = FastAPI()
#     app.include_router(user_router)
#     app.include_router(student_router)
#     app.include_router(course_router)
#
#     app.include_router(employee_router)
#     app.include_router(employee_type_router)
#
#     app.include_router(study_programme_router)
#     app.include_router(year_of_study_router)
#     app.include_router(faculty_router)
#     app.include_router(school_year_router)
#
#     return app
#
#
# app = init_app()
#
#
# @app.get("/", include_in_schema=False)
# def hello_world():
#     return RedirectResponse('/docs')
#
#
# if __name__ == "__main__":
#     uvicorn.run(app)
