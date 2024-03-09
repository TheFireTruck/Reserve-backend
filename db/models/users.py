import uuid
from db.database import Base
from sqlalchemy.sql import func
from sqlalchemy import create_engine, ForeignKey, Boolean, Column, String
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from enum import Enum

class ROLES(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"

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
    profile_picture = Column(String, nullable=False)
    role = Column(SQLAlchemyEnum(ROLES), default=ROLES.USER, nullable=False)

    organisation_id = Column(UUID() , ForeignKey("organisations.id"),nullable=True)
    organisation = relationship("Organisation", back_populates="users")

    github_profile = Column(String)
    twitter_profile = Column(String)
    linkedin_profile = Column(String)
    portfolio_url = Column(String)
    profile_pic_url = Column(String)
    stack_id = Column(Integer, ForeignKey("stacks.id"), nullable=True)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False, server_default=text('now()'))
    updated_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False, server_default=text('now()'), server_onupdate=text("now()"))
    is_active = Column(Boolean)
    status = Column(SQLAlchemyEnum(UserStatus), default=UserStatus.TO_CONTACT, nullable=False)

    skills = relationship('Skill', secondary="users_skills", back_populates='users')
    role = relationship("Role",  back_populates="users")
    tags = relationship('Tag', secondary='users_tags', back_populates='users')
    stack = relationship("Stack", back_populates='users')
    projects = relationship("Project", secondary="users_projects", back_populates="members")
    managed_projects = relationship("Project", back_populates="manager")
    technical_task_submission = relationship("TechnicalTaskSubmission", back_populates="user")
