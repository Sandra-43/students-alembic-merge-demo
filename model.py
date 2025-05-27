from sqlalchemy import Column, Integer, String
from base import Base  # Import Base from your base.py

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
