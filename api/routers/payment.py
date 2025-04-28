from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ..schemas import payment as schema
from ..controllers import payment as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

@router.post("/", response_model=schema.PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(request: schema.PaymentBase, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.PaymentResponse])
def get_all_payments(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{payment_id}", response_model=schema.PaymentResponse)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, payment_id)

@router.put("/{payment_id}", response_model=schema.PaymentResponse)
def update_payment(payment_id: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update(db, payment_id, request)

@router.delete("/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, payment_id)
