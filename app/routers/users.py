from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
)


@router.post(
    "",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    description="Registers a new alumni, student, faculty, or admin in the system.",
)
def create_user(
    user_in: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = crud.get_user_by_email(db, email=user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email address already exists.",
        )
    return crud.create_user(db=db, user_in=user_in)


@router.get(
    "",
    response_model=List[schemas.UserResponse],
    summary="List all users",
    description="Retrieve a paginated list of users with optional filtering by role and search keyword.",
)
def list_users(
    skip: int = Query(default=0, ge=0, description="Number of records to skip"),
    limit: int = Query(default=100, ge=1, le=500, description="Max number of records to return"),
    role: Optional[str] = Query(default=None, description="Filter by role (e.g. alumni, student, faculty, admin)"),
    search: Optional[str] = Query(default=None, description="Filter by name, email, major, or company"),
    db: Session = Depends(get_db),
):
    return crud.get_users(db=db, skip=skip, limit=limit, role=role, search=search)


@router.get(
    "/{user_id}",
    response_model=schemas.UserResponse,
    summary="Get user by ID",
    description="Retrieve detailed profile information for a specific user.",
)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found.",
        )
    return db_user


@router.put(
    "/{user_id}",
    response_model=schemas.UserResponse,
    summary="Update user",
    description="Update an existing user's information.",
)
def update_user(
    user_id: int,
    user_in: schemas.UserUpdate,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found.",
        )

    if user_in.email and user_in.email != db_user.email:
        existing = crud.get_user_by_email(db=db, email=user_in.email)
        if existing and existing.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with this email address already exists.",
            )

    return crud.update_user(db=db, db_user=db_user, user_in=user_in)


@router.delete(
    "/{user_id}",
    summary="Delete user",
    description="Remove a user account from the system.",
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found.",
        )
    crud.delete_user(db=db, db_user=db_user)
    return {"status": "success", "message": f"User {user_id} deleted successfully."}
