import pkgutil
import importlib
from typing import Callable, Set
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.deps.core.logger_instance import LoggerInstance
from api.exceptions.base_exceptions import BaseApplicationException
from api.exceptions.core_exceptions import InternalServerErrorException

def register_exception_handlers(app: FastAPI) -> None:
    def load_all_exceptions() -> None:
        for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
            importlib.import_module(f"{__name__}.{module_name}")

    def get_all_exceptions(cls = BaseApplicationException) -> Set[type[BaseApplicationException]]:
        subclasses = set()
        for subclass in cls.__subclasses__():
            subclasses.add(subclass)
            subclasses.update(get_all_exceptions(subclass))
        return subclasses

    def exception_handler(exc_cls: type[BaseApplicationException]) -> Callable[[Request, Exception], JSONResponse]:
        def wrapper(request: Request, exc: Exception) -> JSONResponse:
            LoggerInstance.get_logger().error(exc, exc_info=exc)
            return exc_cls.get_response()
        return wrapper

    load_all_exceptions()
    for exception_class in get_all_exceptions():
        inner_exception_class = getattr(exception_class, "INNER_EXCEPTION", None)
        app.add_exception_handler(inner_exception_class or exception_class, exception_handler(exception_class))
