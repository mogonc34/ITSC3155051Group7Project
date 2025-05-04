from pydantic import Field, ConfigDict, BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal
from typing_extensions import Annotated

class PromotionBase(BaseModel):
    description: Optional[str] = None
    discount_percent: Annotated[Decimal, Field(ge=0, le=100, max_digits=5, decimal_places=2)]
    expiration_date: Optional[date] = None

class PromotionCreate(PromotionBase):
    promo_code: str  # promo_code is required when creating

class PromotionUpdate(BaseModel):
    description: Optional[str] = None
    discount_percent: Optional[Annotated[Decimal, Field(ge=0, le=100, max_digits=5, decimal_places=2)]] = None
    expiration_date: Optional[date] = None

class PromotionResponse(PromotionBase):
    promo_code: str
    model_config = ConfigDict(from_attributes=True)
