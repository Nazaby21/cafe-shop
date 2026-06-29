from pydantic import BaseModel, EmailStr, ConfigDict


class CreateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: bool

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: EmailStr

class UpdateUserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str | None = None
    is_active: bool