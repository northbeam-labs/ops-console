from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db, Pagination
from app.services.notification import NotificationService
from app.schemas.notification import NotificationIn, NotificationOut

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get("", response_model=list[NotificationOut])
def list_notifications(p: Pagination = Depends(), db: Session = Depends(get_db)):
    return NotificationService(db).list(p)


@router.get("/{id}", response_model=NotificationOut)
def get_notification(id: int, db: Session = Depends(get_db)):
    return NotificationService(db).get(id)


@router.post("", response_model=NotificationOut)
def create_notification(data: NotificationIn, db: Session = Depends(get_db)):
    return NotificationService(db).create(data)
