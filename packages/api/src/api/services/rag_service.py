from api.deps.ollama_query_engine_instance import OllamaQueryEngineInstance

class RAGService:
    @staticmethod
    def query(question: str) -> str:
        return OllamaQueryEngineInstance.get_query_engine().query(question)
