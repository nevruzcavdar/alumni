from typing import List, Optional
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserUpdate


def get_user(db: Session, user_id: int) -> Optional[User]:
    """Retrieve a single user by their primary key ID."""
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Retrieve a single user by unique email address."""
    return db.query(User).filter(User.email == email).first()


def get_users(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    role: Optional[str] = None,
    search: Optional[str] = None,
) -> List[User]:
    """Retrieve a paginated list of users with optional role and search filters."""
    query = db.query(User)

    if role:
        query = query.filter(User.role == role)

    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            (User.full_name.ilike(search_filter))
            | (User.email.ilike(search_filter))
            | (User.major.ilike(search_filter))
            | (User.company.ilike(search_filter))
        )

    return query.offset(skip).limit(limit).all()


def create_user(db: Session, user_in: UserCreate) -> User:
    """Create and persist a new user."""
    db_user = User(
        email=user_in.email,
        full_name=user_in.full_name,
        role=user_in.role,
        graduation_year=user_in.graduation_year,
        major=user_in.major,
        company=user_in.company,
        position=user_in.position,
        bio=user_in.bio,
        is_active=user_in.is_active,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, db_user: User, user_in: UserUpdate) -> User:
    """Update existing user fields."""
    update_data = user_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, db_user: User) -> None:
    """Remove user from database."""
    db.delete(db_user)
    db.commit()
