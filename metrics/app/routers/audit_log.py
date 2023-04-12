from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db, Pagination
from app.services.audit_log import AuditLogService
from app.schemas.audit_log import AuditLogIn, AuditLogOut

router = APIRouter(prefix="/audit_logs", tags=["audit_logs"])


@router.get("", response_model=list[AuditLogOut])
def list_audit_logs(p: Pagination = Depends(), db: Session = Depends(get_db)):
    return AuditLogService(db).list(p)


@router.get("/{id}", response_model=AuditLogOut)
def get_audit_log(id: int, db: Session = Depends(get_db)):
    return AuditLogService(db).get(id)


@router.post("", response_model=AuditLogOut)
def create_audit_log(data: AuditLogIn, db: Session = Depends(get_db)):
    return AuditLogService(db).create(data)
