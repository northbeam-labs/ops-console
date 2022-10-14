from app.repositories.base import BaseRepository
from app.models.organization import Organization


class OrganizationRepository(BaseRepository):
    model = Organization
