from app.repositories.notification import NotificationRepository
from app.models.notification import Notification
from app.exceptions import AppError


class NotificationService:
    def __init__(self, db):
        self.repo = NotificationRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "notification not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(Notification(**data.dict()))
