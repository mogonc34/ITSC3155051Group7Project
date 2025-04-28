from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import ingredient as model
from ..schemas import ingredient as schema

def create(db: Session, request: schema.IngredientCreate):
    new_ingredient = model.Ingredient(
        name=request.name,
        unit=request.unit,
        quantity_available=request.quantity_available
    )
    try:
        db.add(new_ingredient)
        db.commit()
        db.refresh(new_ingredient)
        return new_ingredient
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_all(db: Session):
    try:
        return db.query(model.Ingredient).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def read_one(db: Session, ingredient_id: int):
    try:
        ingredient = db.query(model.Ingredient).filter(model.Ingredient.ingredient_id == ingredient_id).first()
        if not ingredient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient ID not found!")
        return ingredient
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def update(db: Session, ingredient_id: int, request: schema.IngredientUpdate):
    try:
        ingredient_query = db.query(model.Ingredient).filter(model.Ingredient.ingredient_id == ingredient_id)
        ingredient = ingredient_query.first()
        if not ingredient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient ID not found!")

        update_data = request.dict(exclude_unset=True)
        ingredient_query.update(update_data, synchronize_session=False)
        db.commit()
        return ingredient_query.first()
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

def delete(db: Session, ingredient_id: int):
    try:
        ingredient = db.query(model.Ingredient).filter(model.Ingredient.ingredient_id == ingredient_id).first()
        if not ingredient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient ID not found!")
        db.delete(ingredient)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
