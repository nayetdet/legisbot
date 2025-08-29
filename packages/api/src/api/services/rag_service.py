from typing import Optional, Tuple
from api.deps.ollama.ollama_query_engine_instance import OllamaQueryEngineInstance

class RAGService:
    INVALID_RESPONSES: Tuple[str] = (
        "Empty Response",
        "Não encontrei base suficiente para responder com precisão"
    )

    @staticmethod
    def query(question: str) -> Optional[str]:
        query_engine = OllamaQueryEngineInstance.get_query_engine()
        raw_answer = query_engine.query(question)
        if raw_answer and hasattr(raw_answer, "response"):
            response = raw_answer.response.strip()
            if response and response not in RAGService.INVALID_RESPONSES:
                return response
        return None
