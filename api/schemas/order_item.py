from pydantic import BaseModel, EmailStr
from typing import Optional, List

class OrderItemBase(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int
    item_price: float

class OrderItemResponse(OrderItemBase):
    order_item_id: int

    class Config:
        orm_mode = True
