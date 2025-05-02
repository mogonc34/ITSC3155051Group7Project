from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
import uuid
from fastapi import HTTPException
from sqlalchemy import func
from datetime import date
from sqlalchemy.exc import SQLAlchemyError

from ..models import order as model
from ..schemas import order as schema

def get_by_tracking_number(db: Session, tracking_number: str):
    try:
        order = db.query(model.Order).filter(model.Order.tracking_number == tracking_number).first()
        if not order:
            raise HTTPException(status_code=404, detail="Tracking number not found.")
        return order
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e.__dict__.get("orig", e)))

def get_revenue_by_date(db: Session, target_date: date):
    try:
        revenue = db.query(func.sum(model.Order.total_price)) \
            .filter(func.date(model.Order.order_date) == target_date) \
            .scalar()

        return {"date": target_date, "total_revenue": revenue or 0.00}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_orders_by_date_range(db: Session, start_date: date, end_date: date):
    try:
        return db.query(model.Order)\
            .filter(model.Order.order_date >= start_date)\
            .filter(model.Order.order_date <= end_date)\
            .all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e.__dict__.get("orig", str(e))))


def create(db: Session, request: schema.OrderCreate):
    tracking_number = str(uuid.uuid4()).replace("-", "")[:12]  # or your custom logic
    new_order = model.Order(
        customer_id=request.customer_id,
        payment_id=request.payment_id,
        order_status="Processing",
        total_price=request.total_price,
        tracking_number=tracking_number,
        order_type=request.order_type
    )
    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return new_order
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_all(db: Session):
    try:
        return db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_one(db: Session, order_id: int):
    try:
        order = db.query(model.Order).filter(model.Order.order_id == order_id).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order ID not found.")
        return order
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def update(db: Session, order_id: int, request: schema.OrderUpdate):
    try:
        order_query = db.query(model.Order).filter(model.Order.order_id == order_id)
        order = order_query.first()

        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order ID not found.")

        update_data = request.dict(exclude_unset=True)
        order_query.update(update_data, synchronize_session=False)
        db.commit()
        return order_query.first()

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def delete(db: Session, order_id: int):
    try:
        order_query = db.query(model.Order).filter(model.Order.order_id == order_id)
        if not order_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order ID not found.")
        order_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
