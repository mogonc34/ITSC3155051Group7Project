from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ..schemas import rating_review as schema
from ..controllers import rating_review as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/rating-reviews",
    tags=["Rating Reviews"]
)

@router.post("/", response_model=schema.RatingReviewResponse, status_code=status.HTTP_201_CREATED)
def create_rating_review(request: schema.RatingReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.RatingReviewResponse])
def get_all_rating_reviews(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{review_id}", response_model=schema.RatingReviewResponse)
def get_rating_review(review_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, review_id)

@router.put("/{review_id}", response_model=schema.RatingReviewResponse)
def update_rating_review(review_id: int, request: schema.RatingReviewUpdate, db: Session = Depends(get_db)):
    return controller.update(db, review_id, request)

@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rating_review(review_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, review_id)
