from pydantic import BaseModel


class ApiKeyIn(BaseModel):
    name: str
    prefix: str
    revoked: bool


class ApiKeyOut(ApiKeyIn):
    id: int

    class Config:
        from_attributes = True


class ApiKeyUpdate(BaseModel):
    name: str | None = None
    prefix: str | None = None
    revoked: bool | None = None
