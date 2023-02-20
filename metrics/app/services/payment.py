from app.repositories.payment import PaymentRepository
from app.models.payment import Payment
from app.exceptions import AppError


class PaymentService:
    def __init__(self, db):
        self.repo = PaymentRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "payment not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(Payment(**data.dict()))
