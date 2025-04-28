from pydantic import BaseModel

class OrderItemBase(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int
    item_price: float

class OrderItemResponse(OrderItemBase):
    order_item_id: int

    class Config:
        from_attributes = True
