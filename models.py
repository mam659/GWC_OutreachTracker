from sqlalchemy import create_all, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class RecruitmentPoint(Base):
    __tablename__ = 'points'
    id = Column(Integer, primary_key=True)
    member_name = Column(String)
    # Mapping "Extrading", "Contacting", etc. from the PDF 
    category = Column(String) 
    points = Column(Integer, default=25) # Default based on your data [cite: 1]
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
