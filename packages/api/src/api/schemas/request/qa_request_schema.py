from pydantic import BaseModel, Field

class QARequestSchema(BaseModel):
    recordId: str = Field(..., min_length=1)
    question: str = Field(..., min_length=1, max_length=500)
