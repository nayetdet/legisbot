from typing import Optional
from fastapi import UploadFile
from api.mappers.dataset_mapper import DatasetMapper
from api.models.dataset import Dataset
from api.repositories.dataset_repository import DatasetRepository
from api.schemas.response.dataset_response_schema import DatasetResponseSchema
from api.services.ingest_service import IngestService
from api.services.minio_service import MinioService

class DatasetService:
    @staticmethod
    def get_by_id(dataset_id: int) -> Optional[DatasetResponseSchema]:
        dataset: Dataset = DatasetRepository.get_by_id(dataset_id)
        return DatasetMapper.get_response_schema(dataset) if dataset is not None else None

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

    @staticmethod
    def delete_by_id(dataset_id: int) -> None:
        dataset: Dataset = DatasetRepository.get_by_id(dataset_id)
        if dataset is None:
            return

        DatasetRepository.delete_by_dataset(dataset)
        MinioService.delete_by_filename(dataset.name)
        IngestService.delete_by_filename(dataset.name)
