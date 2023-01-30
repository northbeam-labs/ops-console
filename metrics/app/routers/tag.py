from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db, Pagination
from app.services.tag import TagService
from app.schemas.tag import TagIn, TagOut

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("", response_model=list[TagOut])
def list_tags(p: Pagination = Depends(), db: Session = Depends(get_db)):
    return TagService(db).list(p)


@router.get("/{id}", response_model=TagOut)
def get_tag(id: int, db: Session = Depends(get_db)):
    return TagService(db).get(id)


@router.post("", response_model=TagOut)
def create_tag(data: TagIn, db: Session = Depends(get_db)):
    return TagService(db).create(data)
