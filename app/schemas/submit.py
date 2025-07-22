from typing import List
from pydantic import BaseModel

class Answer(BaseModel):
    question_id: int
    selected_option: str  # should be 'a', 'b', 'c', or 'd'

class SubmitQuiz(BaseModel):
    quiz_id: int
    answers: List[Answer]
