from app.repositories.webhook import WebhookRepository
from app.models.webhook import Webhook
from app.exceptions import AppError


class WebhookService:
    def __init__(self, db):
        self.repo = WebhookRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "webhook not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(Webhook(**data.dict()))
# wip: rbac
