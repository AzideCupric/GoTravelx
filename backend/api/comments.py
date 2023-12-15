from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter

from backend import crud, schemas
from backend.deps import get_db, get_current_user

router = APIRouter(prefix="/comments")

# 只能按用户创建comment，不应该凭空创建


@router.get("/", response_model=schemas.Comment, dependencies=[Depends(get_current_user)])
def read_comment(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = crud.get_comments(db, skip=skip, limit=limit)
    return comments
