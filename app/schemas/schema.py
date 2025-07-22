from pydantic import BaseModel, EmailStr
from typing import List, Optional

# ----------------- User -----------------
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

# ----------------- Exam -----------------
class ExamBase(BaseModel):
    title: str
    description: Optional[str] = None

class ExamCreate(ExamBase):
    pass

class ExamOut(ExamBase):
    id: int

    class Config:
        orm_mode = True

# ----------------- Question -----------------
class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    exam_id: int

class QuestionOut(QuestionBase):
    id: int
    exam_id: int

    class Config:
        orm_mode = True

# ----------------- Result -----------------
class ResultBase(BaseModel):
    score: int

class ResultCreate(ResultBase):
    user_id: int
    exam_id: int

class ResultOut(ResultBase):
    id: int
    user_id: int
    exam_id: int

    class Config:
        orm_mode = True
