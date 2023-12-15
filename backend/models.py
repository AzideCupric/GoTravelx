from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    comments = relationship("Comment", back_populates="user")
    histories = relationship("History", back_populates="user")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="comments")


class History(Base):
    __tablename__ = "histories"
    id = Column(Integer, primary_key=True)
    page = Column(String(100), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="history")
