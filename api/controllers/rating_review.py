from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError

from ..models import rating_review as model
from ..schemas import rating_review as schema

def create(db: Session, request):
     new_rating = model.RatingReview(
         rating = request.rating,
         review = request.review
     )

     try:
         db.add(new_rating)
         db.commit()
         db.refresh(new_rating)
     except SQLAlchemyError as e:
         error = str(e.__dict__['orig'])
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

     return new_rating

def read_all(db: Session):
     try:
         result = db.query(model.RatingReview).all()
     except SQLAlchemyError as e:
         error = str(e.__dict__['orig'])
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
     return result

def read_one(db: Session, rating_id: int):
    try:
        rating_review = db.query(model.RatingReview).filter(model.RatingReview.id == rating_id).first()
        if not rating_review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="RatingReview ID not found!")
        return rating_review
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def update(db: Session, rating_id, request):
     try:
         rating_review = db.query(model.RatingReview).filter(model.RatingReview.id == rating_id)
         if not rating_review.first():
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
         update_data = request.dict(exclude_unset=True)
         rating_review.update(update_data, synchronize_session=False)
         db.commit()
     except SQLAlchemyError as e:
         error = str(e.__dict__['orig'])
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
     return rating_review.first()


def delete(db: Session, rating_id):
     try:
         rating_review = db.query(model.RatingReview).filter(model.RatingReview.id == rating_id)
         if not rating_review.first():
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
         rating_review.delete(synchronize_session=False)
         db.commit()
     except SQLAlchemyError as e:
         error = str(e.__dict__['orig'])
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
     return Response(status_code=status.HTTP_204_NO_CONTENT)

