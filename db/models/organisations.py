import uuid
from db.database import Base
from sqlalchemy.sql import func
from sqlalchemy import create_engine, ForeignKey, Boolean, Column, String
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from enum import Enum

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