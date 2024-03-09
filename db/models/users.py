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
    profile_picture = Column(String, nullable=True)
    role = Column(SQLAlchemyEnum(ROLES), default=ROLES.USER, nullable=False)

    organisation_id = Column(UUID() , ForeignKey("organisations.id"),nullable=True)
    organisation = relationship("Organisation", back_populates="users")