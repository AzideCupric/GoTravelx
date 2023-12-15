from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException

from backend import crud, schemas
from backend.deps import get_db, get_current_user

router = APIRouter(prefix="/users")


# 注册新用户不需要token
@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# e.g: /users?skip=0&limit=100
@router.get("/", response_model=list[schemas.User], dependencies=[Depends(get_current_user)])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User, dependencies=[Depends(get_current_user)])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/{user_id}/comments/", response_model=schemas.Comment, dependencies=[Depends(get_current_user)])
def create_comment_for_user(user_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_user_comment(db=db, comment=comment, user_id=user_id)


@router.post("/{user_id}/histories/", response_model=schemas.History, dependencies=[Depends(get_current_user)])
def create_history_for_user(user_id: int, history: schemas.HistoryCreate, db: Session = Depends(get_db)):
    return crud.create_user_history(db=db, history=history, user_id=user_id)
