from pydantic import BaseModel
from typing import Optional, List


# Shared base fields for an order
class OrderBase(BaseModel):
    customer_id: int
    payment_id: Optional[int] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    total_price: float


# Response schema that includes the order_id
class OrderResponse(OrderBase):
    order_id: int

    class Config:
        from_attributes = True


# Order detail input model
class OrderDetailCreate(BaseModel):
    product_id: int
    quantity: int
    unit_price: float


# Main input model for creating an order
class OrderCreate(BaseModel):
    customer_id: int
    order_details: List[OrderDetailCreate]


# Model for updating an order
class OrderUpdate(BaseModel):
    customer_id: int  # or Optional[int] if you want partial update support

    class Config:
        from_attributes = True
