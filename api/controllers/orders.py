from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import order as model
from ..schemas import order as schema

def create(db: Session, request: schema.OrderCreate):
    new_order = model.Order(
        customer_id=request.customer_id,
        payment_id=request.payment_id,
        order_status="Processing",
        total_price=request.total_price
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
