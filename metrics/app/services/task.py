from app.repositories.task import TaskRepository
from app.models.task import Task
from app.exceptions import AppError


class TaskService:
    def __init__(self, db):
        self.repo = TaskRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "task not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(Task(**data.dict()))
