from app.repositories.user import UserRepository
from app.models.user import User
from app.exceptions import AppError


class UserService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    def get(self, id):
        obj = self.repo.get(id)
        if not obj:
            raise AppError(404, "user not found")
        return obj

    def list(self, p):
        return self.repo.list(p.limit, p.offset)

    def create(self, data):
        return self.repo.create(User(**data.dict()))
