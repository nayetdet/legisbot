from minio import Minio
from typing import Optional
from urllib.parse import urlparse
from api.config import Config

class MinioInstance:
    __minio: Optional[Minio] = None

    @classmethod
    def get_minio(cls) -> Minio:
        if cls.__minio is None:
            cls.__minio = Minio(
                endpoint=Config.MINIO_INNER_ENDPOINT,
                access_key=Config.MINIO_ACCESS_KEY,
                secret_key=Config.MINIO_SECRET_KEY,
                secure=urlparse(Config.MINIO_INNER_ENDPOINT).scheme == "https"
            )
        return cls.__minio
