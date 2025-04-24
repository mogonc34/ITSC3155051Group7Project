from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ..schemas import menu_item_ingredients as schema
from ..controllers import menu_item_ingredients as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/menu-item-ingredients",
    tags=["Menu Item Ingredients"]
)

@router.post("/", response_model=schema.MenuItemIngredient, status_code=status.HTTP_201_CREATED)
def create_ingredient_link(request: schema.MenuItemIngredientCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.MenuItemIngredient])
def get_all_ingredient_links(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.MenuItemIngredient)
def get_ingredient_link(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.put("/{item_id}", response_model=schema.MenuItemIngredient)
def update_ingredient_link(item_id: int, request: schema.MenuItemIngredientUpdate, db: Session = Depends(get_db)):
    return controller.update(db, item_id, request)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ingredient_link(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
