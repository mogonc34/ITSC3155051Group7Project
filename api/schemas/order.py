from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderBase(BaseModel):
    customer_id: int
    payment_id: Optional[int] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    order_id: int
    order_date: Optional[datetime] = None

    class Config:
        from_attributes = True
