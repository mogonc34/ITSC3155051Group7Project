from pydantic import ConfigDict, BaseModel
from typing import Optional
from datetime import datetime

class PaymentBase(BaseModel):
    customer_id: int
    payment_type: Optional[str] = None
    card_last_four: Optional[str] = None
    transaction_status: Optional[str] = None

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    payment_type: Optional[str] = None
    card_last_four: Optional[str] = None
    transaction_status: Optional[str] = None

class PaymentResponse(PaymentBase):
    payment_id: int
    transaction_date: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)
