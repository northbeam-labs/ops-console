from pydantic import BaseModel


class InvoiceIn(BaseModel):
    number: str
    amount: float
    currency: str
    paid: bool


class InvoiceOut(InvoiceIn):
    id: int

    class Config:
        from_attributes = True


class InvoiceUpdate(BaseModel):
    number: str | None = None
    amount: float | None = None
    currency: str | None = None
    paid: bool | None = None
