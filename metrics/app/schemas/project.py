from pydantic import BaseModel


class ProjectIn(BaseModel):
    name: str
    description: str
    status: str
    archived: bool


class ProjectOut(ProjectIn):
    id: int

    class Config:
        from_attributes = True


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    status: str | None = None
    archived: bool | None = None
