from app.repositories.base import BaseRepository
from app.models.project import Project


class ProjectRepository(BaseRepository):
    model = Project
