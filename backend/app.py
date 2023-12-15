from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .api import api_router
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
