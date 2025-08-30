import requests
from webui.config import Config
from webui.schemas.request.qa_request_schema import QARequestSchema
from webui.schemas.response.qa_response_schema import QAResponseSchema

class QAService:
    @staticmethod
    def create(request: QARequestSchema) -> QAResponseSchema:
        url: str = f"{Config.WEBUI_API_URL}/v1/qas"
        response = requests.post(url, json=request.model_dump())
        response.raise_for_status()
        return QAResponseSchema.model_validate(response.json())
