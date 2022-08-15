from fastapi import Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Pagination:
    def __init__(self, limit: int = 50, offset: int = 0):
        self.limit = min(limit, 200)
        self.offset = offset
