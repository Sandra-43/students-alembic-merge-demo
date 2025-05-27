from pydantic import BaseModel, EmailStr
from datetime import date

# Shared attributes
class StudentBase(BaseModel):
    name: str
    email: EmailStr
    age: int
    enrolled_date: date

# Create schema
class StudentCreate(StudentBase):
    pass

# Update schema (optional fields)
class StudentUpdate(StudentBase):
    pass

# Response schema
class Student(StudentBase):
    id: int

    model_config = {"from_attributes": True}
