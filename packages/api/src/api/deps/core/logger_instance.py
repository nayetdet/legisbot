import logging

class LoggerInstance:
    __logger: logging.Logger = logging.getLogger("uvicorn.error")

    @classmethod
    def get_logger(cls) -> logging.Logger:
        return cls.__logger
