from typing import Generic, TypeVar, Optional

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")

class ApiResponse(GenericModel, Generic[T]):
    success: bool
    error_code: Optional[str] = None
    message: str
    data: Optional[T] = None


    