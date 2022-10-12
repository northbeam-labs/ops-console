from pydantic import BaseModel


class OrganizationIn(BaseModel):
    name: str
    slug: str
    plan: str
    seats: int


class OrganizationOut(OrganizationIn):
    id: int

    class Config:
        from_attributes = True


class OrganizationUpdate(BaseModel):
    name: str | None = None
    slug: str | None = None
    plan: str | None = None
    seats: int | None = None
