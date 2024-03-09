from database import Base
from sqlalchemy import Column, Integer, String, Boolean,Text,ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    full_name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(Text, nullable=True) 
    profile_pic = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)


    def __repr__(self):
        return f"User(full_name={self.full_name}"
    
