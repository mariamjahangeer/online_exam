from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

# ------------------ User ------------------

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# ------------------ Exam ------------------

def create_exam(db: Session, exam: schemas.ExamCreate):
    db_exam = models.Exam(title=exam.title, description=exam.description)
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam

def get_exam(db: Session, exam_id: int):
    return db.query(models.Exam).filter(models.Exam.id == exam_id).first()


# ------------------ Question ------------------

def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(
        question_text=question.question_text,
        option_a=question.option_a,
        option_b=question.option_b,
        option_c=question.option_c,
        option_d=question.option_d,
        correct_option=question.correct_option,
        exam_id=question.exam_id
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_questions_by_exam(db: Session, exam_id: int):
    return db.query(models.Question).filter(models.Question.exam_id == exam_id).all()


# ------------------ Result ------------------

def submit_result(db: Session, result: schemas.ResultCreate):
    db_result = models.Result(
        user_id=result.user_id,
        exam_id=result.exam_id,
        score=result.score,
        timestamp=datetime.utcnow()
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_results_by_user(db: Session, user_id: int):
    return db.query(models.Result).filter(models.Result.user_id == user_id).all()
