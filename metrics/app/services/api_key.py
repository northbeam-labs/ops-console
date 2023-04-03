from app.repositories.api_key import ApiKeyRepository
from app.models.api_key import ApiKey
from app.exceptions import AppError


class ApiKeyService:
    def __init__(self, db):
        self.repo = ApiKeyRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "api_key not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(ApiKey(**data.dict()))
