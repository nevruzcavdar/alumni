from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from app.database import Base


def utc_now():
    return datetime.now(timezone.utc)


class User(Base):
    """SQLAlchemy model representing an Alumni / System User."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(150), nullable=False)
    role = Column(String(50), default="alumni", nullable=False)  # alumni, student, faculty, admin
    graduation_year = Column(Integer, nullable=True)
    major = Column(String(100), nullable=True)
    company = Column(String(150), nullable=True)
    position = Column(String(150), nullable=True)
    bio = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=utc_now, nullable=False)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now, nullable=False)
