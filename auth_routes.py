from fastapi import APIRouter,status,Depends
from fastapi.exceptions import HTTPException
from database import Session, engine
from schema import SignUpModel,LoginModel
from models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash,check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder


auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


session = Session(bind=engine)