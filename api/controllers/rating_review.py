from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import rating_review as model
from ..schemas import rating_review as schema

def create(db: Session, request: schema.RatingReviewCreate):
    new_item = model.RatingReview(
        customer_id=request.customer_id,
        menu_item_id=request.menu_item_id,
        review_text=request.review_text,
        score=request.score
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_all(db: Session):
    try:
        return db.query(model.RatingReview).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_one(db: Session, review_id: int):
    try:
        item = db.query(model.RatingReview).filter(model.RatingReview.review_id == review_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review ID not found!")
        return item
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def update(db: Session, review_id: int, request: schema.RatingReviewUpdate):
    try:
        item_query = db.query(model.RatingReview).filter(model.RatingReview.review_id == review_id)
        item = item_query.first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review ID not found!")

        update_data = request.dict(exclude_unset=True)
        item_query.update(update_data, synchronize_session=False)
        db.commit()
        return item_query.first()
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def delete(db: Session, review_id: int):
    try:
        item_query = db.query(model.RatingReview).filter(model.RatingReview.review_id == review_id)
        if not item_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review ID not found!")
        item_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
