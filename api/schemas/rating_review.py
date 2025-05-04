from pydantic import Field, ConfigDict, BaseModel
from typing import Optional
from typing_extensions import Annotated

class RatingReviewBase(BaseModel):
    customer_id: int
    menu_item_id: int
    review_text: Optional[str] = None
    score: Annotated[int, Field(ge=1, le=5)]

class RatingReviewCreate(RatingReviewBase):
    pass

class RatingReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    score: Optional[Annotated[int, Field(ge=1, le=5)]] = None

class RatingReviewResponse(RatingReviewBase):
    review_id: int
    model_config = ConfigDict(from_attributes=True)
