from datetime import timedelta

from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from backend.deps import get_db
from backend import crud, schemas
from backend.security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token

router = APIRouter(prefix="/sessions")


@router.post("/login", response_model=schemas.Token)
async def login_for_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = crud.authenticate_user(db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(user.id, expires_delta=access_token_expires),
        "token_type": "bearer",
    }
