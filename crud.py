from db.models import User,Organisation
from db.settings import get_db
from schema.auth import UserSignUp, AdminSignUp
from fastapi import Depends, HTTPException
from passlib.context import CryptContext





pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Operations:
   
    
    
    @staticmethod
    def createuser(user_data:UserSignUp, db:Depends=get_db):
        user_email = db.query(User).filter(User.email == user_data.email).first()
        if user_email:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )
        hash_passwd = Operations.get_password_hash(user_data.password)
        del user_data.password
        


        new_user = User(
            **user_data.dict(),
            password=hash_passwd
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
       



    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)


    @staticmethod
    def verify_password(plain_password, password):
        return pwd_context.verify(plain_password, password)

        