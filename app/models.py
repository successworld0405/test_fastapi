# models.py
from sqlalchemy import Column, String, Float, DateTime, Integer
from sqlalchemy.sql import func
from database import Base

class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    code = Column(String, index=True)
    rate = Column(Float)
    last_update = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
