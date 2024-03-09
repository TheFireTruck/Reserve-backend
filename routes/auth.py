from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from schema.auth import UserSignUp, AdminSignUp, UserResponse
from sqlalchemy.orm import Session
from db.settings import get_db
from db.models import User, Organisation
from utils.utils import get_password_hash
from crud import Operations

auth_router = APIRouter(tags=["Auth"], prefix="/auth")

@auth_router.post('/users/register', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def signup(user: UserSignUp, db: Session = Depends(get_db)):
  created_user = Operations.createuser(user, db)
  return created_user
  

@auth_router.post('/admin/register', status_code=status.HTTP_201_CREATED, response_model=UserSignUp)
async def signup(user: AdminSignUp, db: Session = Depends(get_db)):
    user_email = db.query(User).filter(User.email == user.email).first()
    if user_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hash_passwd = get_password_hash(user.password)

    if user.password != user.password_confirmation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Passwords do not match")

    user.password = hash_passwd

    new_user = user.dict().copy()
    new_user.pop("password_confirmation")

    organisation = Organisation({
        "email": user.organisation_email,
        "name": user.organisation_name
    })

    new_user = User({
        "organisation_id": organisation.id,
        "email": new_user["email"],
        "password": new_user["password"],
        "full_name": new_user["full_name"],
        "role": "admin"
    })

    db.add(organisation)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.refresh(organisation)

    return new_user