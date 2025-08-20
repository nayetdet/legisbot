from fastapi import APIRouter, UploadFile, File
from api.services.dataset_service import DatasetService

router = APIRouter()

@router.get("/{dataset_id}")
def get_by_id(dataset_id: int):
    return DatasetService.get_by_id(dataset_id)

@router.post("/")
def create(file: UploadFile = File(...)):
    return DatasetService.create(file)

@router.delete("/{dataset_id}")
def delete_by_id(dataset_id: int):
    DatasetService.delete_by_id(dataset_id)
