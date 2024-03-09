from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from api.models.auth import UserSignUp
from db.database import get_db

auth_router = APIRouter(tags=["Auth"], prefix="/users")

@auth_router.post('/register', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def signup(user: UserSignUp, db: Session = Depends(get_db)):

    return new_user
