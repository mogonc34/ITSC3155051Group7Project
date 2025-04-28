from pydantic import BaseModel

class OrderPromotionBase(BaseModel):
    order_id: int
    promo_code: str

class OrderPromotionCreate(OrderPromotionBase):
    pass

class OrderPromotionResponse(OrderPromotionBase):
    class Config:
        from_attributes = True
