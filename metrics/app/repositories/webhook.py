from app.repositories.base import BaseRepository
from app.models.webhook import Webhook


class WebhookRepository(BaseRepository):
    model = Webhook
