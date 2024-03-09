from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


class UserSignUp(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    full_name: str = Field(...)
    organisation_id: UUID = Field(...)

class AdminSignUp(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    password_confirmation: str = Field(...)
    full_name: str = Field(...)
    organisation_name: str = Field(...)
    organisation_email: str = Field(...)

class UserResponse(BaseModel):
    id: UUID
    email: str
    full_name: str
    role: str
    organisation_id: UUID
    class Config:
        orm_mode = True