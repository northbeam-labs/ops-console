from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db, Pagination
from app.services.task import TaskService
from app.schemas.task import TaskIn, TaskOut

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=list[TaskOut])
def list_tasks(p: Pagination = Depends(), db: Session = Depends(get_db)):
    return TaskService(db).list(p)


@router.get("/{id}", response_model=TaskOut)
def get_task(id: int, db: Session = Depends(get_db)):
    return TaskService(db).get(id)


@router.post("", response_model=TaskOut)
def create_task(data: TaskIn, db: Session = Depends(get_db)):
    return TaskService(db).create(data)
