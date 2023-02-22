from fastapi import APIRouter, Depends, Response

from app.users.controller import JWTBearer, UserController
from app.users.controller.customer_controller import CustomerController
from app.users.controller.employee_controller import EmployeeController
from app.users.schemas import *

user_router = APIRouter(tags=["Users"], prefix="/api/users")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn) -> object:
    return UserController.create_user(user.email, user.password)


@user_router.post("/add-new-superuser", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_superuser(user: UserSchemaIn) -> object:
    return UserController.create_superuser(user.email, user.password)


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.get("/user-id", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_by_id(user_id: str) -> object:
    return UserController.read_by_id(user_id)


@user_router.get("/email", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_by_email(email: str) -> object:
    return UserController.read_by_email(email)


@user_router.get("/get-all-users", response_model=list[UserSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_all_users() -> list[object]:
    return UserController.read_all()


@user_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_by_id(user_id: str) -> Response:
    return UserController.delete_by_id(user_id)


@user_router.put("/update/active", response_model=UserSchema)
def update_user(user: UserSchemaUpdateActive) -> object:
    return UserController.update_active(user.user_id, user.active)


@user_router.put("/update/password", response_model=UserSchema)
def update_password(user: UserSchemaUpdatePassword) -> object:
    return UserController.update_password(user.email, user.password)


customer_router = APIRouter(tags=["Customers"], prefix="/api/customers")


@customer_router.post("/add-customer-with-shopping-cart", response_model=CustomerSchemaOut)
def create_customer_with_shopping_cart(customer: CustomerSchemaIn) -> object:
    return CustomerController.create_customer_with_shopping_cart(
        customer.name,
        customer.surname,
        customer.phone,
        customer.address,
        customer.city,
        customer.country,
        customer.postal_code,
        customer.user_id,
    )


@customer_router.post(
    "/add-new-customer", response_model=CustomerSchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def create_customer(customer: CustomerSchemaIn) -> object:
    return CustomerController.create(
        customer.name,
        customer.surname,
        customer.phone,
        customer.address,
        customer.city,
        customer.country,
        customer.postal_code,
        customer.user_id,
    )


@customer_router.get("/customer-id", response_model=CustomerSchema)
def get_customer_by_id(customer_id: str) -> object:
    return CustomerController.read_by_id(customer_id)


@customer_router.get(
    "/get-all-customers", response_model=list[CustomerSchema], dependencies=[Depends(JWTBearer("super_user"))]
)
def get_all_customers() -> list[object]:
    return CustomerController.read_all()


@customer_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_customer_by_id(customer_id: str) -> Response:
    return CustomerController.delete_by_id(customer_id)


@customer_router.put("/update/customer", response_model=CustomerSchema)
def update_customer(customer: CustomerSchemaUpdate) -> object:
    return CustomerController.update(
        customer.customer_id,
        customer.name,
        customer.surname,
        customer.phone,
        customer.address,
        customer.city,
        customer.country,
        customer.postal_code,
    )


@customer_router.get("/customer-email", response_model=CustomerSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_customer_by_user_email(email: str) -> object:
    return CustomerController.read_by_email(email)


@customer_router.get(
    "/get-customers-by-phone", response_model=list[CustomerSchema], dependencies=[Depends(JWTBearer("super_user"))]
)
def get_customers_by_phone(phone: str) -> list[object]:
    return CustomerController.read_customers_by_phone(phone)


employee_router = APIRouter(tags=["Employees"], prefix="/api/employees")


@employee_router.post(
    "/add-new-employee", response_model=EmployeeSchema, dependencies=[Depends(JWTBearer("super_user"))]
)
def create_employee(employee: EmployeeSchemaIn) -> object:
    return EmployeeController.create(
        employee.name, employee.surname, employee.phone, employee.job_title, employee.user_id, employee.office_id
    )


@employee_router.get("/employee-id", response_model=EmployeeSchema)
def get_employee_by_id(employee_id: str) -> object:
    return EmployeeController.read_by_id(employee_id)


@employee_router.get("/get-all-employees", response_model=list[EmployeeSchema])
def get_all_employees() -> list[object]:
    return EmployeeController.read_all()


@employee_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_employee_by_id(employee_id: str) -> Response:
    return EmployeeController.delete_by_id(employee_id)


@employee_router.put("/update/employee", response_model=EmployeeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_employee(employee: EmployeeSchemaUpdate) -> object:
    return EmployeeController.update(
        employee.employee_id, employee.name, employee.surname, employee.phone, employee.job_title
    )
