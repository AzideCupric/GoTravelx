"""定义依赖注入所使用的函数"""

from typing import Annotated

from jose import JWTError, jwt
from sqlalchemy.orm import Session
from pydantic import ValidationError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from .models import User
from .schemas import TokenPayload
from .database import SessionLocal
from .security import ALGORITHM, SECRET_KEY

reuseable_oauth2 = OAuth2PasswordBearer(tokenUrl="/sessions/token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(reuseable_oauth2)]


def get_current_user(session: SessionDep, token: TokenDep):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
        )
    user = session.get(User, token_data.sub)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
