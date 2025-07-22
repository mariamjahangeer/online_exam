from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import ExamCreate, ExamResponse
from app.crud import create_exam, get_exam
from app.database import get_db

router = APIRouter(prefix="/exams", tags=["Exams"])

@router.post("/", response_model=ExamResponse)
def create_new_exam(exam: ExamCreate, db: Session = Depends(get_db)):
    return create_exam(db, exam)

@router.get("/{exam_id}", response_model=ExamResponse)
def read_exam(exam_id: int, db: Session = Depends(get_db)):
    db_exam = get_exam(db, exam_id)
    if not db_exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return db_exam
