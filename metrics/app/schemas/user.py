from pydantic import BaseModel


class UserIn(BaseModel):
    email: str
    full_name: str
    is_active: bool
    hashed_password: str


class UserOut(UserIn):
    id: int

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    email: str | None = None
    full_name: str | None = None
    is_active: bool | None = None
    hashed_password: str | None = None
