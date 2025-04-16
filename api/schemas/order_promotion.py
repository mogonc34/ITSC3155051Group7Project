from pydantic import BaseModel

class OrderPromotionBase(BaseModel):
    order_id: int
    promo_code: str

    class Config:
        from_attributes = True
