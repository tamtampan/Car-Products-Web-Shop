class UserNotFoundError(Exception):
    def __init__(self, message="User not found.", code=400):
        self.message = message
        self.code = code


class UserInvalidPassword(Exception):
    def __init__(self, message="Invalid password provided.", code=400):
        self.message = message
        self.code = code


class UserPasswordLenError(Exception):
    def __init__(self, message="Password must contain at least 6 characters.", code=400):
        self.message = message
        self.code = code


class UserNotSuperUser(Exception):
    def __init__(self, message="User is not superuser.", code=400):
        self.message = message
        self.code = code


class CustomerNotFoundError(Exception):
    def __init__(self, message="Customer not found.", code=400):
        self.message = message
        self.code = code


class EmployeeNotFoundError(Exception):
    def __init__(self, message="Employee not found.", code=400):
        self.message = message
        self.code = code
