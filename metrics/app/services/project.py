from app.repositories.project import ProjectRepository
from app.models.project import Project
from app.exceptions import AppError


class ProjectService:
    def __init__(self, db):
        self.repo = ProjectRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "project not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(Project(**data.dict()))
