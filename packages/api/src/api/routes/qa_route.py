from fastapi import APIRouter, UploadFile, File
from api.schemas.request.qa_request_schema import QARequestSchema
from api.services.qa_service import QAService

router = APIRouter()

@router.get("/{qa_id}")
def get_by_id(qa_id: int):
    return QAService.get_by_id(qa_id)

@router.post("/")
def create(request: QARequestSchema):
    return QAService.create(request)

@router.delete("/{qa_id}")
def delete_by_id(qa_id: int):
    QAService.delete_by_id(qa_id)
