from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import QuestionCreate, QuestionResponse
from app.crud import create_question, get_questions_by_exam
from app.database import get_db

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.post("/", response_model=QuestionResponse)
def add_question(question: QuestionCreate, db: Session = Depends(get_db)):
    return create_question(db, question)

@router.get("/exam/{exam_id}", response_model=list[QuestionResponse])
def list_questions_for_exam(exam_id: int, db: Session = Depends(get_db)):
    return get_questions_by_exam(db, exam_id)
