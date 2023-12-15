from datetime import datetime

from pydantic import BaseModel


class CommentBase(BaseModel):
    content: str
    timestamp: datetime


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class HistoryBase(BaseModel):
    page: str
    timestamp: datetime


class HistoryCreate(HistoryBase):
    pass


class History(HistoryBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserSecret(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    comments: list[Comment] = []
    histories: list[History] = []

    class Config:
        from_attributes = True


# JSON payload containing access token
class Token(BaseModel):
    access_token: str
    token_type: str


# Contents of JWT token
class TokenPayload(BaseModel):
    sub: int | None = None
