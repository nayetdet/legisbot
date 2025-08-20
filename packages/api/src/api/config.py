from os import getenv

class Config:
    # PostgreSQL
    POSTGRES_DATABASE_URL: str = getenv("POSTGRES_DATABASE_URL")

    # MinIO
    MINIO_INNER_ENDPOINT: str = getenv("MINIO_INNER_ENDPOINT")
    MINIO_OUTER_ENDPOINT: str = getenv("MINIO_OUTER_ENDPOINT")
    MINIO_ACCESS_KEY: str = getenv("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY: str = getenv("MINIO_SECRET_KEY")
