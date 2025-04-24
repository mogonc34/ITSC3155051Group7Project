from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..schemas import payment as schema
from ..controllers import payment as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

@router.post("/", response_model=schema.Payment, status_code=status.HTTP_201_CREATED)
def create_payment(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/order/{order_id}", response_model=schema.Payment)
def get_payment_by_order(order_id: int, db: Session = Depends(get_db)):
    return controller.get_by_order(db, order_id)
