from pydantic import BaseModel


class CommentIn(BaseModel):
    body: str
    author_id: int
    edited: bool


class CommentOut(CommentIn):
    id: int

    class Config:
        from_attributes = True


class CommentUpdate(BaseModel):
    body: str | None = None
    author_id: int | None = None
    edited: bool | None = None
