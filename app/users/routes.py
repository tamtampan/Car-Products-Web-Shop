from fastapi import APIRouter, Depends
from app.users.controller import UserController
from app.users.controller.customer_controller import CustomerController
from app.users.controller.employee_controller import EmployeeController
from app.users.schemas import *
from app.users.controller.user_authentication_controller import JWTBearer

user_router = APIRouter(tags=["Users"], prefix="/api/users")


# dependencies=[Depends(JWTBearer("super_user"))]


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.email, user.password)


@user_router.post("/add-new-superuser", response_model=UserSchema)
def create_superuser(user: UserSchemaIn):
    return UserController.create_superuser(user.email, user.password)


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.get("/user-id", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_by_id(user_id: str):
    return UserController.read_by_id(user_id)


@user_router.get("/email", response_model=UserSchema)
def get_by_email(email: str):
    return UserController.read_by_email(email)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.read_all()


@user_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_by_id(user_id: str):
    return UserController.delete_by_id(user_id)


@user_router.put("/update/active", response_model=UserSchema)
def update_user(user_id: str, active: bool):
    return UserController.update_active(user_id, active)


customer_router = APIRouter(tags=["Customers"], prefix="/api/customers")


# dependencies=[Depends(JWTBearer("super_user"))]


@customer_router.post("/add-new-customer", response_model=CustomerSchema)
def create_customer(customer: CustomerSchemaIn):
    return CustomerController.create(customer.name, customer.surname, customer.phone, customer.address,
                                     customer.city, customer.country, customer.postal_code, customer.user_id)


@customer_router.get("/customer-id", response_model=CustomerSchema)
def get_customer_by_id(customer_id: str):
    return CustomerController.read_by_id(customer_id)


@customer_router.get("/get-all-customers", response_model=list[CustomerSchema])
def get_all_customers():
    return CustomerController.read_all()


@customer_router.delete("/")
def delete_customer_by_id(customer_id: str):
    return CustomerController.delete_by_id(customer_id)


@customer_router.put("/update/customer", response_model=CustomerSchema)
def update_customer(customer_id: str, name: str = None, surname: str = None, phone: str = None, address: str = None,
                    city: str = None, country: str = None, postal_code: str = None):
    return CustomerController.update(customer_id, name, surname, phone, address, city, country, postal_code)


employee_router = APIRouter(tags=["Employees"], prefix="/api/employees")


# dependencies=[Depends(JWTBearer("super_user"))]

@employee_router.post("/add-new-employee", response_model=EmployeeSchema)
def create_employee(employee: EmployeeSchemaIn):
    return EmployeeController.create(employee.name, employee.surname, employee.phone, employee.job_title,
                                     employee.user_id)


@employee_router.get("/employee-id", response_model=EmployeeSchema)
def get_employee_by_id(employee_id: str):
    return EmployeeController.read_by_id(employee_id)


@employee_router.get("/get-all-employees", response_model=list[EmployeeSchema])
def get_all_employees():
    return EmployeeController.read_all()


@employee_router.delete("/")
def delete_employee_by_id(employee_id: str):
    return EmployeeController.delete_by_id(employee_id)


@employee_router.put("/update/employee", response_model=EmployeeSchema)
def update_employee(employee_id: str, name: str = None, surname: str = None, phone: str = None, job_title: str = None):
    return EmployeeController.update(employee_id, name, surname, phone, job_title)
