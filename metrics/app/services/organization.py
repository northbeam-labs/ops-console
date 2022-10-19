from app.repositories.organization import OrganizationRepository
from app.models.organization import Organization
from app.exceptions import AppError


class OrganizationService:
    def __init__(self, db):
        self.repo = OrganizationRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "organization not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(Organization(**data.dict()))
