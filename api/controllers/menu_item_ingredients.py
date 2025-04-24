from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import menu_item_ingredients as model
from ..schemas import menu_item_ingredients as schema


def create(db: Session, request: schema.MenuItemIngredientCreate):
    new_entry = model.MenuItemIngredient(
        menu_item_id=request.menu_item_id,
        ingredient_id=request.ingredient_id,
        amount=request.amount
    )

    try:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return new_entry
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_all(db: Session):
    try:
        return db.query(model.MenuItemIngredient).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_one(db: Session, item_id: int):
    try:
        item = db.query(model.MenuItemIngredient).filter(model.MenuItemIngredient.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MenuItemIngredient ID not found.")
        return item
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def update(db: Session, item_id: int, request: schema.MenuItemIngredientCreate):
    try:
        item_query = db.query(model.MenuItemIngredient).filter(model.MenuItemIngredient.id == item_id)
        item = item_query.first()

        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MenuItemIngredient ID not found.")

        update_data = request.dict(exclude_unset=True)
        item_query.update(update_data, synchronize_session=False)
        db.commit()
        return item_query.first()
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def delete(db: Session, item_id: int):
    try:
        item_query = db.query(model.MenuItemIngredient).filter(model.MenuItemIngredient.id == item_id)
        if not item_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MenuItemIngredient ID not found.")
        item_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
