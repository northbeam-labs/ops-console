from sqlalchemy.orm import Session


class BaseRepository:
    model = None

    def __init__(self, db: Session):
        self.db = db

    def get(self, id):
        return self.db.query(self.model).get(id)

    def list(self, limit=50, offset=0):
        return self.db.query(self.model).offset(offset).limit(limit).all()

    def create(self, obj):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, obj):
        self.db.delete(obj)
        self.db.commit()
