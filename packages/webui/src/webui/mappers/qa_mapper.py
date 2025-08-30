from webui.schemas.request.qa_request_schema import QARequestSchema

class QAMapper:
    @staticmethod
    def to_request(question: str) -> QARequestSchema:
        return QARequestSchema(question=question)
