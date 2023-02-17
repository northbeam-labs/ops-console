from app.repositories.base import BaseRepository
from app.models.payment import Payment


class PaymentRepository(BaseRepository):
    model = Payment
