from pydantic import BaseModel
from typing import List

class QuizCreate(BaseModel):
    title: str

class ShowQuiz(BaseModel):
    id: int
    title: str
    class Config:
        orm_mode = True
