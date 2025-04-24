from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ..schemas import order as schema
from ..controllers import orders as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/", response_model=schema.Order, status_code=status.HTTP_201_CREATED)
def create_order(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.Order])
def get_all_orders(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.Order)
def get_order(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.put("/{item_id}", response_model=schema.Order)
def update_order(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db, item_id, request)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
