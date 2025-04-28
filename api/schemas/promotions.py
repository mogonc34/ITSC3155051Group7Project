from pydantic import BaseModel, condecimal
from typing import Optional
from datetime import date

class PromotionBase(BaseModel):
    description: Optional[str] = None
    discount_percent: condecimal(ge=0, le=100, max_digits=5, decimal_places=2)
    expiration_date: Optional[date] = None

class PromotionCreate(PromotionBase):
    promo_code: str  # promo_code is required when creating

class PromotionResponse(PromotionBase):
    promo_code: str

    class Config:
        from_attributes = True
