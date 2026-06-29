from email import message

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.schemas.user_schema import CreateUserRequest, UserResponse, UpdateUserRequest
from app.services.user_service import UserService
from app.schemas.api_response import ApiResponse

router = APIRouter(prefix="/user", tags=["user"])

user_service = UserService()

@router.post("", response_model=UserResponse)
def create_user(request: CreateUserRequest,db: Session = Depends(get_db)):
    return user_service.create_user(db, request)

@router.get("", response_model=list[UserResponse])
def read_all_users(db: Session = Depends(get_db)):
    return user_service.get_all_user(db)

@router.get("/{user_id}", response_model=ApiResponse[UserResponse])
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    return ApiResponse(
        success=True,
        message="User fetched successfully",
        data=user
    )


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    request: UpdateUserRequest,
    db: Session = Depends(get_db)
):
    return user_service.update_user(db, user_id, request)
