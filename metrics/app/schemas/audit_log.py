from pydantic import BaseModel


class AuditLogIn(BaseModel):
    action: str
    actor_id: int
    target: str


class AuditLogOut(AuditLogIn):
    id: int

    class Config:
        from_attributes = True


class AuditLogUpdate(BaseModel):
    action: str | None = None
    actor_id: int | None = None
    target: str | None = None
