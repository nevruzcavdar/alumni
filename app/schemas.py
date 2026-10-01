from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    """Base schema with shared user attributes."""
    email: str = Field(..., description="Unique email address of the user", examples=["alumni@university.edu"])
    full_name: str = Field(..., description="Full name of the user", examples=["Nevruz Çavdar"])
    role: str = Field(default="alumni", description="Role (alumni, student, faculty, admin)", examples=["alumni"])
    graduation_year: Optional[int] = Field(default=None, description="Year of graduation", examples=[2024])
    major: Optional[str] = Field(default=None, description="Academic department / major", examples=["Computer Engineering"])
    company: Optional[str] = Field(default=None, description="Current employer", examples=["Tech Corp"])
    position: Optional[str] = Field(default=None, description="Job title", examples=["Software Engineer"])
    bio: Optional[str] = Field(default=None, description="Short biography", examples=["Passionate about AI and cloud systems."])
    is_active: bool = Field(default=True, description="Account active status")


class UserCreate(UserBase):
    """Schema for creating a new user."""
    pass


class UserUpdate(BaseModel):
    """Schema for updating an existing user (all fields optional)."""
    email: Optional[str] = Field(default=None, description="Updated email address")
    full_name: Optional[str] = Field(default=None, description="Updated full name")
    role: Optional[str] = Field(default=None, description="Updated role")
    graduation_year: Optional[int] = Field(default=None, description="Updated graduation year")
    major: Optional[str] = Field(default=None, description="Updated major")
    company: Optional[str] = Field(default=None, description="Updated company")
    position: Optional[str] = Field(default=None, description="Updated position")
    bio: Optional[str] = Field(default=None, description="Updated biography")
    is_active: Optional[bool] = Field(default=None, description="Updated active status")


class UserResponse(UserBase):
    """Schema for returning user details."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
