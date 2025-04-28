from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import order_promotion as model
from ..models.order_promotion import OrderPromotion
from ..schemas import order_promotion as schema

def create(db: Session, request):
    oder_promo = model.OrderPromotion(
        order_id = request.id,
        promotion_id = request.promotion_id,
    )
    db.add(oder_promo)
    db.commit()
    db.refresh(oder_promo)
    return oder_promo

def read_all(db: Session):
    try:
        return db.query(model.OrderPromotion).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

def read_one(db: Session, order_promotion_id: int):
    try:
        order_promo = db.query(model.OrderPromotion).filter(model.OrderPromotion.id == order_promotion_id).first()
        if not order_promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found!")
        return order_promo
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    def update_promotion(db: Session, order_promotion: schema.OrderPromotion):

    def delete(db: Session, order_promotion: schema.OrderPromotion):