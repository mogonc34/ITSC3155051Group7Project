from pydantic import ConfigDict, BaseModel
from typing import Optional
from datetime import datetime

class OrderBase(BaseModel):
    customer_id: int
    payment_id: Optional[int] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None
    tracking_number: Optional[str] = None
    order_type: str

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    payment_id: Optional[int] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None

class OrderResponse(OrderBase):
    order_id: int
    order_date: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)
