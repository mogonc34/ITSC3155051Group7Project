from pydantic import BaseModel
from typing import Optional


class RatingReviewBase(BaseModel):
    rating: int
    review: Optional[str] = None
    customer_id: int
    sandwich_id: int


class RatingReviewCreate(RatingReviewBase):
    pass


class RatingReview(RatingReviewBase):
    id: int

    class Config:
        from_attributes = True
