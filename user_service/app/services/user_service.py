from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import CreateUserRequest, UpdateUserRequest
from app.repository import user_repository as user_repo
from app.core.exception import EmailAlreadyExists, UserNotFound


class UserService:

    def create_user(self, db: Session, request: CreateUserRequest):
        existing_email = user_repo.get_by_email(db, request.email)
        if existing_email:
            raise EmailAlreadyExists(request.email)

        data = request.model_dump()

        data["username"] = data["username"].strip()
        data["is_active"] = True

        user = User(**data)

        return user_repo.create(db, user)

    def get_all_user(self, db: Session):
        return user_repo.get_all(db)

    def get_user_by_id(self, db: Session, user_id: int):
        user = user_repo.get_by_id(db, user_id)
        if not user:
            raise UserNotFound(user_id)
        return user

    def update_user(self, db: Session, user_id: int, request: UpdateUserRequest):
        user = user_repo.get_by_id(db, user_id)
        if not user:
            raise UserNotFound(user_id)

        if user.email != request.email:
            email_exists = user_repo.get_by_email(db, request.email)
            if email_exists:
                raise EmailAlreadyExists(request.email)

        user.username = request.username.strip()
        user.email = request.email
        user.password = request.password
        user.is_active = request.is_active

        db.commit()
        db.refresh(user)

        return user