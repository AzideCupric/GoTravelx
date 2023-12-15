from sqlalchemy.orm import Session

from . import models, schemas
from .security import verify_password, get_password_hash


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_name(db, username)
    if not user:
        return False
    if not verify_password(password, str(user.hashed_password)):
        return False
    return user


def get_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).offset(skip).limit(limit).all()


def create_user_comment(db: Session, comment: schemas.CommentCreate, user_id: int):
    db_item = models.Comment(**comment.model_dump(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_histories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.History).offset(skip).limit(limit).all()


def create_user_history(db: Session, history: schemas.HistoryCreate, user_id: int):
    db_item = models.History(**history.model_dump(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
