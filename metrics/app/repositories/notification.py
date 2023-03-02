from app.repositories.base import BaseRepository
from app.models.notification import Notification


class NotificationRepository(BaseRepository):
    model = Notification
