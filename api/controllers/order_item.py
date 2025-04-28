from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import order_item as model
from ..schemas import order_item as schema

def create(db: Session, request):
    new_order = model.OrderItem(
        order_id=request.order_id,
        menu_item_id=request.menu_item_id,
        quantity=request.quantity,
        item_price=request.item_price,
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def read_all(db: Session):
    try:
        return db.query(model.OrderItem).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found!")

def read_one(db:Session, order_id: int):
    try:
        order = db.query(model.OrderItem).filter(model.OrderItem.order_id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found!")
    return order

def update(db: Session, order_id: int, item: schema.OrderItemResponse):
    try:
        promo_query = db.query(model.OrderItem).filter(model.OrderItem.id == order_id)
        promo = promo_query.first()

        if not promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found!")

        update_data = request.dict(exclude_unset=True)
        promo_query.update(update_data, synchronize_session=False)
        db.commit()
        return promo_query.first()
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def delete(db: Session, order_id: int, order_item_id):
    try:
        order_item = db.query(model.OrderItem).filter(model.OrderItem == order_item_id).first()
        if not order_item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found!")
        order_item.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

