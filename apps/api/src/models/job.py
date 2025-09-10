from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    tags = Column(ARRAY(String))
    salary_min = Column(Integer)
    salary_max = Column(Integer)
    description = Column(Text, nullable=False)
    company = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
