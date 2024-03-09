from pydantic import BaseModel, EmailStr, Field

class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


class UserSignUp(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    full_name: str = Field(...)
    role: str = Field(...)