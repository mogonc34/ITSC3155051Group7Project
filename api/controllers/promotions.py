from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import promotions as model
from ..schemas import promotions as schema

def create(db: Session, request: schema.PromotionCreate):
    new_promo = model.Promotion(
        promo_code=request.promo_code,
        description=request.description,
        discount_percent=request.discount_percent,
        expiration_date=request.expiration_date
    )

    try:
        db.add(new_promo)
        db.commit()
        db.refresh(new_promo)
        return new_promo
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_all(db: Session):
    try:
        return db.query(model.Promotion).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_one(db: Session, promo_code: str):
    try:
        promo = db.query(model.Promotion).filter(model.Promotion.promo_code == promo_code).first()
        if not promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
        return promo
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def update(db: Session, promo_code: str, request: schema.PromotionUpdate):
    try:
        promo_query = db.query(model.Promotion).filter(model.Promotion.promo_code == promo_code)
        promo = promo_query.first()

        if not promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")

        update_data = request.dict(exclude_unset=True)
        promo_query.update(update_data, synchronize_session=False)
        db.commit()
        return promo_query.first()
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def delete(db: Session, promo_code: str):
    try:
        promo_query = db.query(model.Promotion).filter(model.Promotion.promo_code == promo_code)
        if not promo_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion not found!")
        promo_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
