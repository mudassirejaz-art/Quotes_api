from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(100), index=True)
    text = Column(Text, nullable=False)
    category = Column(String(50), nullable=True)
