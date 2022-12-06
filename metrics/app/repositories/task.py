from app.repositories.base import BaseRepository
from app.models.task import Task


class TaskRepository(BaseRepository):
    model = Task
