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
from fastapi import HTTPException
from app.auth.hashing import verify
from app.auth.jwt_handler import create_access_token
from app.schemas.user import UserLogin

@router.post("/login")
def login(request: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify(request.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    token = create_access_token(data={"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}
