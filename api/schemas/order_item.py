from pydantic import BaseModel
from typing import Optional

class OrderItemBase(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int
    item_price: float

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(BaseModel):
    quantity: Optional[int] = None
    item_price: Optional[float] = None

class OrderItemResponse(OrderItemBase):
    order_item_id: int

    class Config:
        from_attributes = True
