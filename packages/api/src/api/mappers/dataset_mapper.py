from api.config import Config
from api.models.dataset import Dataset
from api.schemas.response.dataset_response_schema import DatasetResponseSchema

class DatasetMapper:
    @staticmethod
    def get_response_schema(dataset: Dataset) -> DatasetResponseSchema:
        return DatasetResponseSchema(
            id=dataset.id,
            name=dataset.name,
            url=f"{Config.MINIO_OUTER_ENDPOINT}/{Config.MINIO_BUCKET}/{dataset.name}",
            content_type=dataset.content_type,
            size_in_bytes=dataset.size_in_bytes,
            created_at=dataset.created_at,
            updated_at=dataset.updated_at
        )
