from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ..schemas import menu_item as schema
from ..controllers import menu_item as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/menu-items",
    tags=["Menu Items"]
)

@router.post("/", response_model=schema.MenuItemResponse, status_code=status.HTTP_201_CREATED)
def create_menu_item(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.MenuItemResponse])
def get_all_menu_items(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{menu_item_id}", response_model=schema.MenuItemResponse)
def get_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, menu_item_id)

@router.get("/category/{category}", response_model=list[schema.MenuItemResponse])
def get_menu_item_by_category(category: str, db: Session = Depends(get_db)):
    return controller.get_by_food_category(db, category)

@router.put("/{menu_item_id}", response_model=schema.MenuItemResponse)
def update_menu_item(menu_item_id: int, request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db, menu_item_id, request)

@router.delete("/{menu_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, menu_item_id)
