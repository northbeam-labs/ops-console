from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db, Pagination
from app.services.invoice import InvoiceService
from app.schemas.invoice import InvoiceIn, InvoiceOut

router = APIRouter(prefix="/invoices", tags=["invoices"])


@router.get("", response_model=list[InvoiceOut])
def list_invoices(p: Pagination = Depends(), db: Session = Depends(get_db)):
    return InvoiceService(db).list(p)


@router.get("/{id}", response_model=InvoiceOut)
def get_invoice(id: int, db: Session = Depends(get_db)):
    return InvoiceService(db).get(id)


@router.post("", response_model=InvoiceOut)
def create_invoice(data: InvoiceIn, db: Session = Depends(get_db)):
    return InvoiceService(db).create(data)
