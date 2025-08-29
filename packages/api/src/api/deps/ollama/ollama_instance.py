from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from api.config import Config

class OllamaInstance:
    __llm: Ollama = Ollama(host=Config.OLLAMA_HOST_URL, model=Config.OLLAMA_LLM_MODEL, request_timeout=6000)
    __embedding: OllamaEmbedding = OllamaEmbedding(model_name=Config.OLLAMA_EMBEDDING_MODEL, embed_batch_size=16)

    @classmethod
    def get_llm(cls) -> Ollama:
        return cls.__llm

    @classmethod
    def get_embedding(cls) -> OllamaEmbedding:
        return cls.__embedding
