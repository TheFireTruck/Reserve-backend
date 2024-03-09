from pydantic import BaseModel, EmailStr, Field

class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


class UserSignUp(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    full_name: str = Field(...)
    organisation_id: str = Field(...)

class AdminSignUp(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    password_confirmation: str = Field(...)
    full_name: str = Field(...)
    organisation_name: str = Field(...)
    organisation_email: str = Field(...)

class UserResponse(BaseModel):
    id: str
    email: str
    full_name: str
    role: str
    organisation_id: str
    class Config:
        orm_mode = True