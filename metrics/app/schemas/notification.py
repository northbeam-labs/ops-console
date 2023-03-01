from pydantic import BaseModel


class NotificationIn(BaseModel):
    kind: str
    message: str
    read: bool


class NotificationOut(NotificationIn):
    id: int

    class Config:
        from_attributes = True


class NotificationUpdate(BaseModel):
    kind: str | None = None
    message: str | None = None
    read: bool | None = None
