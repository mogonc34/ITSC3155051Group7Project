from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

from ..models import payment as model
from ..schemas import payment as schema


def create(db: Session, request: schema.PaymentBase):
    new_payment = model.Payment(
        customer_id=request.customer_id,
        payment_type=request.payment_type,
        card_last_four=request.card_last_four,
        transaction_status=request.transaction_status or "success",
        payment_date=datetime.utcnow()
    )

    try:
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
        return new_payment
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Payment creation failed: {error}")


def read_all(db: Session):
    try:
        return db.query(model.Payment).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Could not fetch payments: {error}")


def read_one(db: Session, payment_id: int):
    try:
        payment = db.query(model.Payment).filter(model.Payment.id == payment_id).first()
        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found.")
        return payment
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error retrieving payment: {error}")
