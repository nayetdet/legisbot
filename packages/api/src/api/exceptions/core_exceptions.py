from fastapi import status
from typing import ClassVar
from api.exceptions.base_exceptions import BaseApplicationException

class InternalServerErrorException(BaseApplicationException):
    STATUS_CODE: ClassVar[int] = status.HTTP_500_INTERNAL_SERVER_ERROR
    MESSAGE: ClassVar[str] = "An internal server error occurred."
    INNER_EXCEPTION: ClassVar[type[Exception]] = Exception
