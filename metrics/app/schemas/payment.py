from pydantic import BaseModel


class PaymentIn(BaseModel):
    amount: float
    provider: str
    status: str
    reference: str


class PaymentOut(PaymentIn):
    id: int

    class Config:
        from_attributes = True


class PaymentUpdate(BaseModel):
    amount: float | None = None
    provider: str | None = None
    status: str | None = None
    reference: str | None = None
