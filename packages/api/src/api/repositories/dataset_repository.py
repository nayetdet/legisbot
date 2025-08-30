from typing import Optional
from api.deps.databases.postgres_instance import PostgresInstance
from api.models.dataset import Dataset

class DatasetRepository:
    @staticmethod
    def get_by_id(dataset_id: int) -> Optional[Dataset]:
        with PostgresInstance().get_db() as session:
            return session.get(Dataset, dataset_id)

    @staticmethod
    def create(dataset: Dataset) -> Dataset:
        with PostgresInstance.get_db() as session:
            session.add(dataset)
            session.commit()
            session.refresh(dataset)
        return dataset

    @staticmethod
    def delete_by_dataset(dataset: Dataset) -> None:
        with PostgresInstance.get_db() as session:
            session.delete(dataset)
            session.commit()
            session.refresh(dataset)
