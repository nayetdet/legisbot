from io import BytesIO
from time import time
from fastapi import UploadFile
from api.config import Config
from api.deps.databases.minio_instance import MinioInstance

class MinioService:
    @staticmethod
    def create(file: UploadFile) -> str:
        filename: str = f"{int(time() * 1000)}_{file.filename}"
        MinioInstance.get_minio().put_object(
            bucket_name=Config.MINIO_BUCKET,
            object_name=filename,
            data=BytesIO(file.file.read()),
            length=file.size,
            content_type=file.content_type
        )

        return filename

    @staticmethod
    def delete_by_filename(filename: str) -> None:
        MinioInstance.get_minio().remove_object(
            bucket_name=Config.MINIO_BUCKET,
            object_name=filename
        )
