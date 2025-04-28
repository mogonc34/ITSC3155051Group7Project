from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import order_promotion as model
from ..schemas import order_promotion as schema

def create(db: Session, request: schema.OrderPromotionCreate):
    new_entry = model.OrderPromotion(
        order_id=request.order_id,
        promo_code=request.promo_code
    )
    try:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return new_entry
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_all(db: Session):
    try:
        return db.query(model.OrderPromotion).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_one(db: Session, order_id: int, promo_code: str):
    try:
        entry = db.query(model.OrderPromotion).filter(
            model.OrderPromotion.order_id == order_id,
            model.OrderPromotion.promo_code == promo_code
        ).first()
        if not entry:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderPromotion not found.")
        return entry
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def delete(db: Session, order_id: int, promo_code: str):
    try:
        entry_query = db.query(model.OrderPromotion).filter(
            model.OrderPromotion.order_id == order_id,
            model.OrderPromotion.promo_code == promo_code
        )
        if not entry_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderPromotion not found.")
        entry_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
