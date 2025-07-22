from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class ShowUser(BaseModel):
    id: int
    email: EmailStr
    class Config:
        from_attributes = True
class UserLogin(BaseModel):
    email: EmailStr
    password: str
