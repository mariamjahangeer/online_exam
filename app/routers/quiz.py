from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.quiz import Quiz
from app.models.question import Question
from app.schemas.quiz import QuizCreate, ShowQuiz
from app.schemas.question import QuestionCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/quiz")
def create_quiz(quiz: QuizCreate, db: Session = Depends(get_db)):
    new_quiz = Quiz(title=quiz.title)
    db.add(new_quiz)
    db.commit()
    db.refresh(new_quiz)
    return new_quiz

@router.post("/question")
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    new_q = Question(**question.dict())
    db.add(new_q)
    db.commit()
    db.refresh(new_q)
    return new_q
from app.schemas.submit import SubmitQuiz

@router.post("/submit")
def submit_quiz(payload: SubmitQuiz, db: Session = Depends(get_db)):
    correct = 0
    total = 0

    for ans in payload.answers:
        question = db.query(Question).filter(Question.id == ans.question_id, Question.quiz_id == payload.quiz_id).first()
        if question:
            total += 1
            if question.correct_answer.lower() == ans.selected_option.lower():
                correct += 1

    return {
        "quiz_id": payload.quiz_id,
        "total_questions": total,
        "correct_answers": correct,
        "score_percent": (correct / total * 100) if total else 0
    }
