from fastapi import FastAPI
from app.core.database import Base, engine

from app.models.user import User
from app.api.user_route import router as user_router
from app.core.exception import ApplicationError
from app.core.exception_handler import (application_error_handler)

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(user_router)
app.add_exception_handler(ApplicationError, application_error_handler)

