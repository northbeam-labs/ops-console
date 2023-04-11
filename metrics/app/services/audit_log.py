from app.repositories.audit_log import AuditLogRepository
from app.models.audit_log import AuditLog
from app.exceptions import AppError


class AuditLogService:
    def __init__(self, db):
        self.repo = AuditLogRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "audit_log not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(AuditLog(**data.dict()))
