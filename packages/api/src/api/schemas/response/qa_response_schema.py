from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class QAResponseSchema(BaseModel):
    id: Optional[int] = None
    question: Optional[str] = None
    answer: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
