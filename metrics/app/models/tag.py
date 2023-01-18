from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.sql import func
from app.db import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(255), nullable=True)
    color = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
