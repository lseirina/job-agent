from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func
from .base import Base

class Vacancy(Base):
    __tablename__ = "vacancies"
    
    id = Column(Integer, primary_key=True, index=True)
    hh_id = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    url = Column(String)
    company = Column(String)
    salary = Column(String)
    description = Column(Text)
    skills = Column(Text)
    experience = Column(String)
    employment_type = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    processed = Column(Boolean, default=False)
    relevance_score = Column(Integer, default=0)
    
    def __repr__(self):
        return f"<Vacancy {self.name} at {self.company}>"