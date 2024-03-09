import uuid
from db.settings import Base
from sqlalchemy.sql import func
from sqlalchemy import create_engine, ForeignKey, Boolean, Column, String, String, Integer, TIMESTAMP, text
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from enum import Enum





class User(Base):
    __tablename__ = "users"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=func.uuid_generate_v4(),
        default=uuid.uuid4,
    )
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    profile_picture = Column(String, nullable=True)
    role = Column(String, default="user", nullable=False)


    organisation_id = Column(UUID() , ForeignKey("organisations.id"), nullable=True)
    organisation = relationship("Organisation", back_populates="users")




class Organisation(Base):
    __tablename__ = "organisations"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=func.uuid_generate_v4(),
        default=uuid.uuid4,
    )
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    users = relationship("User", back_populates="organisation")

