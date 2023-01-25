from app.repositories.base import BaseRepository
from app.models.tag import Tag


class TagRepository(BaseRepository):
    model = Tag
