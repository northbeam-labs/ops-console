from pydantic import BaseModel


class TagIn(BaseModel):
    label: str
    color: str


class TagOut(TagIn):
    id: int

    class Config:
        from_attributes = True


class TagUpdate(BaseModel):
    label: str | None = None
    color: str | None = None
