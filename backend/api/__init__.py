from fastapi import APIRouter

from . import users, comments, sessions, histories

api_router = APIRouter()
api_router.include_router(users.router, tags=["users"])
api_router.include_router(comments.router, tags=["comments"])
api_router.include_router(histories.router, tags=["histories"])
api_router.include_router(sessions.router, tags=["sessions"])
