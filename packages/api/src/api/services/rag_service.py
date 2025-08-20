from typing import Optional
from api.deps.llms.ollama_query_engine_instance import OllamaQueryEngineInstance

class RAGService:
    @staticmethod
    def query(question: str) -> Optional[str]:
        raw_answer = OllamaQueryEngineInstance.get_query_engine().query(question)
        return raw_answer.response if hasattr(raw_answer, "response") else None
