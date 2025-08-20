import re
from abc import ABC
from datetime import datetime, timezone
from typing import ClassVar
from fastapi.responses import JSONResponse

class BaseApplicationException(ABC, Exception):
    STATUS_CODE: ClassVar[int]
    MESSAGE: ClassVar[str]
    INNER_EXCEPTION: ClassVar[type[Exception]]

    @classmethod
    def get_response(cls) -> JSONResponse:
        return JSONResponse(
            status_code=cls.STATUS_CODE,
            content={
                "status": cls.STATUS_CODE,
                "code": re.sub(r"([a-z])([A-Z])", r"\1_\2", cls.__name__).upper(),
                "message": cls.MESSAGE,
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        )
