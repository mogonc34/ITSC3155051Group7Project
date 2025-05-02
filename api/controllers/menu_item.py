from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import menu_item as model
from ..schemas import menu_item as schema
from sqlalchemy.exc import SQLAlchemyError

def get_by_food_category(db: Session, category: str):
    try:
        items = db.query(model.MenuItem).filter(model.MenuItem.food_category == category).all()
        if not items:
            raise HTTPException(status_code=404, detail="No items found in this food category.")
        return items
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e.__dict__.get("orig", e)))

def create(db: Session, request: schema.MenuItemCreate):
    new_item = model.MenuItem(
        name=request.name,
        description=request.description,
        price=request.price,
        calories=request.calories,
        food_category=request.food_category
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_all(db: Session):
    try:
        return db.query(model.MenuItem).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_one(db: Session, menu_item_id: int):
    try:
        item = db.query(model.MenuItem).filter(model.MenuItem.menu_item_id == menu_item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item ID not found!")
        return item
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def update(db: Session, menu_item_id: int, request: schema.MenuItemUpdate):
    try:
        item_query = db.query(model.MenuItem).filter(model.MenuItem.menu_item_id == menu_item_id)
        item = item_query.first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item ID not found!")

        update_data = request.dict(exclude_unset=True)
        item_query.update(update_data, synchronize_session=False)
        db.commit()
        return item_query.first()
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def delete(db: Session, menu_item_id: int):
    try:
        item_query = db.query(model.MenuItem).filter(model.MenuItem.menu_item_id == menu_item_id)
        item = item_query.first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item ID not found!")
        item_query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
