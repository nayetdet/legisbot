from minio import Minio
from typing import Optional
from urllib.parse import urlparse
from api.config import Config

class MinioInstance:
    __minio: Optional[Minio] = None

    @classmethod
    def get_minio(cls) -> Minio:
        if cls.__minio is None:
            parsed_inner_endpoint = urlparse(Config.MINIO_INNER_ENDPOINT)
            cls.__minio = Minio(
                endpoint=parsed_inner_endpoint.netloc or parsed_inner_endpoint.path,
                access_key=Config.MINIO_ACCESS_KEY,
                secret_key=Config.MINIO_SECRET_KEY,
                secure=parsed_inner_endpoint.scheme == "https"
            )
        return cls.__minio
