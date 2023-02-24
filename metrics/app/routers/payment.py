from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db, Pagination
from app.services.payment import PaymentService
from app.schemas.payment import PaymentIn, PaymentOut

router = APIRouter(prefix="/payments", tags=["payments"])


@router.get("", response_model=list[PaymentOut])
def list_payments(p: Pagination = Depends(), db: Session = Depends(get_db)):
    return PaymentService(db).list(p)


@router.get("/{id}", response_model=PaymentOut)
def get_payment(id: int, db: Session = Depends(get_db)):
    return PaymentService(db).get(id)


@router.post("", response_model=PaymentOut)
def create_payment(data: PaymentIn, db: Session = Depends(get_db)):
    return PaymentService(db).create(data)
