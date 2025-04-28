from pydantic import BaseModel, conint
from typing import Optional

class RatingReviewBase(BaseModel):
    customer_id: int
    menu_item_id: int
    review_text: Optional[str] = None
    score: conint(ge=1, le=5)
class RatingReviewCreate(RatingReviewBase):
    pass

class RatingReviewResponse(RatingReviewBase):
    review_id: int

    class Config:
        from_attributes = True
