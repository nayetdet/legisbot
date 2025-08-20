from abc import ABC
from datetime import datetime, timezone
from sqlalchemy import Integer, Column, DateTime
from api.models import Base

class BaseModel(Base, ABC):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
