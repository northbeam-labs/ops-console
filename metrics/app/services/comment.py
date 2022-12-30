from app.repositories.comment import CommentRepository
from app.models.comment import Comment
from app.exceptions import AppError


class CommentService:
    def __init__(self, db):
        self.repo = CommentRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "comment not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(Comment(**data.dict()))
