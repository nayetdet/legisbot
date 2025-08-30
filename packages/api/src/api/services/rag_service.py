from typing import Optional, Tuple
from api.deps.ollama.ollama_query_engine_instance import OllamaQueryEngineInstance

class RAGService:
    @staticmethod
    def query(question: str) -> Optional[str]:
        query_engine = OllamaQueryEngineInstance.get_query_engine()
        raw_answer = query_engine.query(question)
        return raw_answer.response if hasattr(raw_answer, "response") else None
