from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, ShowUser
from app.auth.hashing import hash

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=ShowUser)
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(email=user.email, hashed_password=hash(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
