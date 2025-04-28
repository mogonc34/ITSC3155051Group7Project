from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ..schemas import order_promotion as schema
from ..controllers import order_promotion as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/order-promotions",
    tags=["Order Promotions"]
)

@router.post("/", response_model=schema.OrderPromotionResponse, status_code=status.HTTP_201_CREATED)
def create_order_promotion(request: schema.OrderPromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.OrderPromotionResponse])
def get_all_order_promotions(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_id}/{promo_code}", response_model=schema.OrderPromotionResponse)
def get_order_promotion(order_id: int, promo_code: str, db: Session = Depends(get_db)):
    return controller.read_one(db, order_id, promo_code)

@router.delete("/{order_id}/{promo_code}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order_promotion(order_id: int, promo_code: str, db: Session = Depends(get_db)):
    return controller.delete(db, order_id, promo_code)
