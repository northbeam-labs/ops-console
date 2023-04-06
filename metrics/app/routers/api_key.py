from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db, Pagination
from app.services.api_key import ApiKeyService
from app.schemas.api_key import ApiKeyIn, ApiKeyOut

router = APIRouter(prefix="/api_keys", tags=["api_keys"])


@router.get("", response_model=list[ApiKeyOut])
def list_api_keys(p: Pagination = Depends(), db: Session = Depends(get_db)):
    return ApiKeyService(db).list(p)


@router.get("/{id}", response_model=ApiKeyOut)
def get_api_key(id: int, db: Session = Depends(get_db)):
    return ApiKeyService(db).get(id)


@router.post("", response_model=ApiKeyOut)
def create_api_key(data: ApiKeyIn, db: Session = Depends(get_db)):
    return ApiKeyService(db).create(data)
