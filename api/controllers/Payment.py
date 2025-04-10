from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime

from ..models import payments as model
from ..models.orders import Order
from ..schemas import payments as schema


def create(db: Session, request: schema.PaymentCreate):
    # Check if the order exists
    order = db.query(Order).filter(Order.id == request.order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found.")

    # Create a new payment record
    payment = model.Payment(
        order_id=request.order_id,
        payment_type=request.payment_type,
        card_number=request.card_number,
        transaction_status="success",  # Assume it goes through
        amount=request.amount,
        payment_date=datetime.utcnow()
    )

    try:
        db.add(payment)
        db.commit()
        db.refresh(payment)
        return payment
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Payment failed")


def get_by_order(db: Session, order_id: int):
    payment = db.query(model.Payment).filter(model.Payment.order_id == order_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found.")
    return payment
