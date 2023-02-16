class UserNotFoundException(Exception):
    def __init__(self, message="User not found.", code=400):
        self.message = message
        self.code = code


class UserInvalidPassword(Exception):
    def __init__(self, message="Invalid password provided.", code=400):
        self.message = message
        self.code = code


class UserNotSuperUser(Exception):
    def __init__(self, message="User is not superuser.", code=400):
        self.message = message
        self.code = code


class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer not found.", code=400):
        self.message = message
        self.code = code


class EmployeeNotFoundException(Exception):
    def __init__(self, message="Employee not found.", code=400):
        self.message = message
        self.code = code
