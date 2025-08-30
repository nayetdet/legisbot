from typing import Optional
from fastapi import UploadFile
from api.exceptions.dataset_exceptions import DatasetNotFoundException
from api.mappers.dataset_mapper import DatasetMapper
from api.models.dataset import Dataset
from api.repositories.dataset_repository import DatasetRepository
from api.schemas.response.dataset_response_schema import DatasetResponseSchema
from api.services.ingest_service import IngestService
from api.services.minio_service import MinioService

class DatasetService:
    @staticmethod
    def get_by_id(dataset_id: int) -> Optional[DatasetResponseSchema]:
        dataset: Optional[Dataset] = DatasetRepository.get_by_id(dataset_id)
        if dataset is None:
            raise DatasetNotFoundException()
        return DatasetMapper.get_response_schema(dataset)

    @staticmethod
    def create(file: UploadFile) -> DatasetResponseSchema:
        filename: str = MinioService.create(file)
        try:
            dataset: Dataset = Dataset(
                name=filename,
                size_in_bytes=file.size,
                content_type=file.content_type
            )

            dataset = DatasetRepository.create(dataset)
            IngestService.ingest(file, filename)
            return DatasetMapper.get_response_schema(dataset)
        except Exception as e:
            MinioService.delete_by_filename(filename)
            raise e
