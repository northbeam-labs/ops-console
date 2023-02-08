from app.repositories.base import BaseRepository
from app.models.invoice import Invoice


class InvoiceRepository(BaseRepository):
    model = Invoice
