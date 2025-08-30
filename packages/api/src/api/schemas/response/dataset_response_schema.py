from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class DatasetResponseSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    url: Optional[str] = None
    content_type: Optional[str] = None
    size_in_bytes: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
