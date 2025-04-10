from pydantic import BaseModel

class OrderPromotionBase(BaseModel):
    order_id: int
    promo_code: str

    class Config:
        orm_mode = True
