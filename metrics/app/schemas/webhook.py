from pydantic import BaseModel


class WebhookIn(BaseModel):
    url: str
    event: str
    active: bool
    secret: str


class WebhookOut(WebhookIn):
    id: int

    class Config:
        from_attributes = True


class WebhookUpdate(BaseModel):
    url: str | None = None
    event: str | None = None
    active: bool | None = None
    secret: str | None = None
