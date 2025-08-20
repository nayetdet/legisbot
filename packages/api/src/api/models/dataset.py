from sqlalchemy import Column, String, BigInteger
from api.models.base_model import BaseModel

class Dataset(BaseModel):
    __tablename__ = "datasets"

    name = Column(String, nullable=False)
    content_type = Column(String(length=50), nullable=False)
    size_in_bytes = Column(BigInteger, nullable=False)
