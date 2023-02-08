from app.repositories.invoice import InvoiceRepository
from app.models.invoice import Invoice
from app.exceptions import AppError


class InvoiceService:
    def __init__(self, db):
        self.repo = InvoiceRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "invoice not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(Invoice(**data.dict()))
