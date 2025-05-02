from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError
from decimal import Decimal

from ..models import order_item as model
from ..models import menu_item_ingredients as mii_model
from ..models import ingredient as ingredient_model
from ..schemas import order_item as schema



def create(db: Session, request: schema.OrderItemCreate):
    new_order_item = model.OrderItem(
        order_id=request.order_id,
        menu_item_id=request.menu_item_id,
        quantity=request.quantity,
        item_price=request.item_price
    )
    try:
        ingredients_required = db.query(mii_model.MenuItemIngredient).filter_by(menu_item_id=request.menu_item_id).all()

        for req in ingredients_required:
            ingredient = db.query(ingredient_model.Ingredient).filter_by(ingredient_id=req.ingredient_id).first()

            total_needed = Decimal(req.quantity_required) * Decimal(request.quantity)
            available = Decimal(ingredient.quantity_available)

            if available < total_needed:
                raise HTTPException(
                    status_code=400,
                    detail=f"Not enough {ingredient.name}: required {total_needed}, available {available}"
                )
        db.add(new_order_item)
        for req in ingredients_required:
            ingredient = db.query(ingredient_model.Ingredient).filter_by(ingredient_id=req.ingredient_id).first()
            total_needed = req.quantity_required * request.quantity
            ingredient.quantity_available -= total_needed
        db.commit()
        db.refresh(new_order_item)
        return new_order_item
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_all(db: Session):
    try:
        return db.query(model.OrderItem).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_one(db: Session, order_item_id: int):
    try:
        order_item = db.query(model.OrderItem).filter(model.OrderItem.order_item_id == order_item_id).first()
        if not order_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderItem ID not found.")
        return order_item
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def update(db: Session, order_item_id: int, request: schema.OrderItemUpdate):
    try:
        order_item_query = db.query(model.OrderItem).filter(model.OrderItem.order_item_id == order_item_id)
        order_item = order_item_query.first()

        if not order_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderItem ID not found.")

        update_data = request.dict(exclude_unset=True)
        order_item_query.update(update_data, synchronize_session=False)
        db.commit()
        return order_item_query.first()
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def delete(db: Session, order_item_id: int):
    try:
        order_item_query = db.query(model.OrderItem).filter(model.OrderItem.order_item_id == order_item_id)
        if not order_item_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderItem ID not found.")
        order_item_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
