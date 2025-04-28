from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ..schemas import order_item as schema
from ..controllers import order_item as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/order-items",
    tags=["Order Items"]
)

@router.post("/", response_model=schema.OrderItemResponse, status_code=status.HTTP_201_CREATED)
def create_order_item(request: schema.OrderItemCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.OrderItemResponse])
def get_all_order_items(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_item_id}", response_model=schema.OrderItemResponse)
def get_order_item(order_item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_item_id)

@router.put("/{order_item_id}", response_model=schema.OrderItemResponse)
def update_order_item(order_item_id: int, request: schema.OrderItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db, order_item_id, request)

@router.delete("/{order_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, order_item_id)
