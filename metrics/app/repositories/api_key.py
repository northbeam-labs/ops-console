from app.repositories.base import BaseRepository
from app.models.api_key import ApiKey


class ApiKeyRepository(BaseRepository):
    model = ApiKey
