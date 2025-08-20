from fastapi import status
from typing import ClassVar
from api.exceptions.base_exceptions import BaseApplicationException

class DatasetNotFoundException(BaseApplicationException):
    STATUS_CODE: ClassVar[int] = status.HTTP_404_NOT_FOUND
    MESSAGE: ClassVar[str] = "The request dataset was not found."
