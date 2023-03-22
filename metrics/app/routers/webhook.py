from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db, Pagination
from app.services.webhook import WebhookService
from app.schemas.webhook import WebhookIn, WebhookOut

router = APIRouter(prefix="/webhooks", tags=["webhooks"])


@router.get("", response_model=list[WebhookOut])
def list_webhooks(p: Pagination = Depends(), db: Session = Depends(get_db)):
    return WebhookService(db).list(p)


@router.get("/{id}", response_model=WebhookOut)
def get_webhook(id: int, db: Session = Depends(get_db)):
    return WebhookService(db).get(id)


@router.post("", response_model=WebhookOut)
def create_webhook(data: WebhookIn, db: Session = Depends(get_db)):
    return WebhookService(db).create(data)
