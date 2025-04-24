from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ..schemas import menu_item as schema
from ..controllers import menu_item as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/menu-items",
    tags=["Menu Items"]
)

@router.post("/", response_model=schema.MenuItem, status_code=status.HTTP_201_CREATED)
def create_menu_item(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.MenuItem])
def get_all_menu_items(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.MenuItem)
def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.put("/{item_id}", response_model=schema.MenuItem)
def update_menu_item(item_id: int, request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db, item_id, request)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
