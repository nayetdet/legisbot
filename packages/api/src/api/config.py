from os import getenv
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API
    API_CORS_ORIGINS: List[str] = [x.strip() for x in (getenv("API_CORS_ORIGINS") or "").split(",") if x.strip()]

    # Ollama
    OLLAMA_HOST_URL: str = getenv("OLLAMA_HOST_URL")
    OLLAMA_LLM_MODEL: str = getenv("OLLAMA_LLM_MODEL")
    OLLAMA_EMBEDDING_MODEL: str = getenv("OLLAMA_EMBEDDING_MODEL")

    # PostgreSQL
    POSTGRES_HOST_URL: str = getenv("POSTGRES_HOST_URL")

    # ChromaDB
    CHROMA_HOST_URL: str = getenv("CHROMA_HOST_URL")
    CHROMA_COLLECTION_NAME: str = getenv("CHROMA_COLLECTION_NAME")

    # MinIO
    MINIO_INNER_ENDPOINT: str = getenv("MINIO_INNER_ENDPOINT")
    MINIO_OUTER_ENDPOINT: str = getenv("MINIO_OUTER_ENDPOINT")
    MINIO_BUCKET: str = getenv("MINIO_BUCKET")
    MINIO_ACCESS_KEY: str = getenv("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY: str = getenv("MINIO_SECRET_KEY")
