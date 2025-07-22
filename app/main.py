from fastapi import FastAPI
from app.database import db
from app.routers import user

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Online Exam API is working!"}

