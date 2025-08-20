from api.models.qa import QA
from api.schemas.request.qa_request_schema import QARequestSchema
from api.schemas.response.qa_response_schema import QAResponseSchema

class QAMapper:
    @staticmethod
    def to_qa(request: QARequestSchema) -> QA:
        return QA(
            question=request.question,
            answer=request.answer
        )

    @staticmethod
    def to_response_schema(qa: QA) -> QAResponseSchema:
        return QAResponseSchema(
            id=qa.id,
            question=qa.question,
            answer=qa.answer,
            created_at=qa.created_at,
            updated_at=qa.updated_at
        )
