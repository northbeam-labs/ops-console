from app.repositories.base import BaseRepository
from app.models.comment import Comment


class CommentRepository(BaseRepository):
    model = Comment
