from pydantic import BaseModel, EmailStr
from typing import Optional, List

class OrderBase(BaseModel):
    customer_id: int
    payment_id: Optional[int]
    tracking_number: Optional[str]
    order_status: Optional[str]
    total_price: float

class OrderResponse(OrderBase):
    order_id: int

    class Config:
        orm_mode = True
