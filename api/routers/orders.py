from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from datetime import date

from ..schemas import order as schema
from ..controllers import orders as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/", response_model=schema.OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/revenue/{target_date}")
def get_revenue(target_date: date, db: Session = Depends(get_db)):
    return controller.get_revenue_by_date(db, target_date)

@router.get("/track/{tracking_number}", response_model=schema.OrderResponse)
def track_order(tracking_number: str, db: Session = Depends(get_db)):
    return controller.get_by_tracking_number(db, tracking_number)

@router.get("/date-range/")
def get_orders_in_range(start_date: date, end_date: date, db: Session = Depends(get_db)):
    return controller.get_orders_by_date_range(db, start_date, end_date)

@router.get("/", response_model=list[schema.OrderResponse])
def get_all_orders(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_id}", response_model=schema.OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_id)

@router.put("/{order_id}", response_model=schema.OrderResponse)
def update_order(order_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db, order_id, request)

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, order_id)
