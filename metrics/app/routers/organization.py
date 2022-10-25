from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db, Pagination
from app.services.organization import OrganizationService
from app.schemas.organization import OrganizationIn, OrganizationOut

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.get("", response_model=list[OrganizationOut])
def list_organizations(p: Pagination = Depends(), db: Session = Depends(get_db)):
    return OrganizationService(db).list(p)


@router.get("/{id}", response_model=OrganizationOut)
def get_organization(id: int, db: Session = Depends(get_db)):
    return OrganizationService(db).get(id)


@router.post("", response_model=OrganizationOut)
def create_organization(data: OrganizationIn, db: Session = Depends(get_db)):
    return OrganizationService(db).create(data)
