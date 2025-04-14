from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PromotionBase(BaseModel):
    promotion_name: str
    promotion_description: str
    promotion_start_date: datetime
    promotion_end_date: datetime


class PromotionCreate(PromotionBase):
    pass


class Promotion(PromotionBase):
    id: int

    class Config:
        from_attributes = True
