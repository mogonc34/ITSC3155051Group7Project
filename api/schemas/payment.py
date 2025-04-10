from pydantic import BaseModel, EmailStr
from typing import Optional, List

class PaymentBase(BaseModel):
    customer_id: int
    payment_type: Optional[str]
    card_last_four: Optional[str]
    transaction_status: Optional[str]

class PaymentResponse(PaymentBase):
    payment_id: int

    class Config:
        orm_mode = True
