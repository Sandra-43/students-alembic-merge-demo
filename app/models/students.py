from sqlalchemy import Column, Integer, String, Date
from app.database.db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)
    enrolled_date = Column(Date, nullable=False)
    address = Column(Integer, nullable=True)