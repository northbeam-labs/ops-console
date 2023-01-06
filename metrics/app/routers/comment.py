from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db, Pagination
from app.services.comment import CommentService
from app.schemas.comment import CommentIn, CommentOut

router = APIRouter(prefix="/comments", tags=["comments"])


@router.get("", response_model=list[CommentOut])
def list_comments(p: Pagination = Depends(), db: Session = Depends(get_db)):
    return CommentService(db).list(p)


@router.get("/{id}", response_model=CommentOut)
def get_comment(id: int, db: Session = Depends(get_db)):
    return CommentService(db).get(id)


@router.post("", response_model=CommentOut)
def create_comment(data: CommentIn, db: Session = Depends(get_db)):
    return CommentService(db).create(data)
