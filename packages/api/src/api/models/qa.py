from sqlalchemy import Column, String, Text
from api.models.base_model import BaseModel

class QA(BaseModel):
    __tablename__ = "qas"

    question = Column(String(500), nullable=False)
    answer = Column(Text)
