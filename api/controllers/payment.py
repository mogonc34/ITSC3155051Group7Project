from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import payment as model
from ..schemas import payment as schema

def create(db: Session, request: schema.PaymentBase):
    new_payment = model.Payment(
        customer_id=request.customer_id,
        payment_type=request.payment_type,
        card_last_four=request.card_last_four,
        transaction_status=request.transaction_status or "success"
        # transaction_date is auto-filled by database with server_default=func.now()
    )

    try:
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
        return new_payment
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Payment creation failed: {error}"
        )

def read_all(db: Session):
    try:
        return db.query(model.Payment).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not fetch payments: {error}"
        )

def read_one(db: Session, payment_id: int):
    try:
        payment = db.query(model.Payment).filter(model.Payment.payment_id == payment_id).first()
        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found.")
        return payment
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error retrieving payment: {error}"
        )

def update(db: Session, payment_id: int, request: schema.PaymentUpdate):
    try:
        payment_query = db.query(model.Payment).filter(model.Payment.payment_id == payment_id)
        payment = payment_query.first()

        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found.")

        update_data = request.dict(exclude_unset=True)
        payment_query.update(update_data, synchronize_session=False)
        db.commit()
        return payment_query.first()
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Payment update failed: {error}"
        )

def delete(db: Session, payment_id: int):
    try:
        payment_query = db.query(model.Payment).filter(model.Payment.payment_id == payment_id)
        payment = payment_query.first()

        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found.")

        payment_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Payment deletion failed: {error}"
        )
