from os import getenv
from typing import List

class Config:
    # API
    API_CORS_ORIGINS: List[str] = [x.strip() for x in (getenv("API_CORS_ORIGINS") or "").split(",") if x.strip()]

    # Ollama
    OLLAMA_HOST_URL: str = getenv("OLLAMA_HOST_URL")
    OLLAMA_LLM_MODEL: str = getenv("OLLAMA_LLM_MODEL")
    OLLAMA_EMBEDDING_MODEL: str = getenv("OLLAMA_EMBEDDING_MODEL")

    # PostgreSQL
    POSTGRES_HOST_URL: str = getenv("POSTGRES_HOST_URL")

    # Elasticsearch
    ELASTICSEARCH_HOST_URL: str = getenv("ELASTICSEARCH_HOST_URL")

    # MinIO
    MINIO_INNER_ENDPOINT: str = getenv("MINIO_INNER_ENDPOINT")
    MINIO_OUTER_ENDPOINT: str = getenv("MINIO_OUTER_ENDPOINT")
    MINIO_BUCKET: str = getenv("MINIO_BUCKET")
    MINIO_ACCESS_KEY: str = getenv("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY: str = getenv("MINIO_SECRET_KEY")
