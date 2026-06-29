from http import HTTPStatus

class ApplicationError(Exception):
    def __init__(self, message: str, error_code: str, status_code: int):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code

        super().__init__(message)


class UserNotFound(ApplicationError):
    def __init__(self, user_id: int):
        super().__init__(
            message = f"User with id {user_id} not found",
            error_code= "err_404",
            status_code= HTTPStatus.NOT_FOUND
        )

class EmailAlreadyExists(ApplicationError):
    def __init__(self, email: str):
        super().__init__(
            message= f"Email {email} already exists",
            error_code= "err_409",
            status_code=HTTPStatus.CONFLICT
        )