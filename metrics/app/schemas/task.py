from pydantic import BaseModel


class TaskIn(BaseModel):
    title: str
    priority: int
    done: bool
    due_date: str


class TaskOut(TaskIn):
    id: int

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    title: str | None = None
    priority: int | None = None
    done: bool | None = None
    due_date: str | None = None
