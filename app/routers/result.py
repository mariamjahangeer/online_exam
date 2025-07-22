from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import ResultCreate, ResultResponse
from app.curd import submit_result, get_results_by_user
from app.database import get_db

router = APIRouter(prefix="/results", tags=["Results"])

@router.post("/", response_model=ResultResponse)
def submit_exam_result(result: ResultCreate, db: Session = Depends(get_db)):
    return submit_result(db, result)

@router.get("/user/{user_id}", response_model=list[ResultResponse])
def get_user_results(user_id: int, db: Session = Depends(get_db)):
    return get_results_by_user(db, user_id)
