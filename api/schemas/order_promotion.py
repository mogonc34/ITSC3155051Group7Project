from pydantic import ConfigDict, BaseModel

class OrderPromotionBase(BaseModel):
    order_id: int
    promo_code: str

class OrderPromotionCreate(OrderPromotionBase):
    pass

class OrderPromotionResponse(OrderPromotionBase):
    model_config = ConfigDict(from_attributes=True)
