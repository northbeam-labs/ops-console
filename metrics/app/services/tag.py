from app.repositories.tag import TagRepository
from app.models.tag import Tag
from app.exceptions import AppError


class TagService:
    def __init__(self, db):
        self.repo = TagRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "tag not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(Tag(**data.dict()))
