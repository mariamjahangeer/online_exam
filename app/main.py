from fastapi import FastAPI
from app.routers import auth
from app.database.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
from app.routers import quiz

app.include_router(quiz.router)
