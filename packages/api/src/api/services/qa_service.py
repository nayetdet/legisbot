from typing import Optional
from api.exceptions.qa_exceptions import QANotFoundException
from api.mappers.qa_mapper import QAMapper
from api.models.qa import QA
from api.repositories.qa_repository import QARepository
from api.schemas.request.qa_request_schema import QARequestSchema
from api.schemas.response.qa_response_schema import QAResponseSchema
from api.services.rag_service import RAGService

class QAService:
    @staticmethod
    def get_by_id(qa_id: int) -> Optional[QAResponseSchema]:
        qa: Optional[QA] = QARepository.get_by_id(qa_id)
        if qa is None:
            raise QANotFoundException()
        return QAMapper.to_response_schema(qa)

    @staticmethod
    def create(request: QARequestSchema) -> QAResponseSchema:
        answer: Optional[str] = RAGService.query(request.question)
        qa: QA = QARepository.create(QAMapper.to_qa(request, answer))
        return QAMapper.to_response_schema(qa)

    @staticmethod
    def delete_by_id(qa_id: int) -> None:
        QARepository.delete_by_id(qa_id)
