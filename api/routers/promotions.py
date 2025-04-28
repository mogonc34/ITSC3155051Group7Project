from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ..schemas import promotions as schema
from ..controllers import promotions as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/promotions",
    tags=["Promotions"]
)

@router.post("/", response_model=schema.PromotionResponse, status_code=status.HTTP_201_CREATED)
def create_promotion(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.PromotionResponse])
def get_all_promotions(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{promo_code}", response_model=schema.PromotionResponse)
def get_promotion(promo_code: str, db: Session = Depends(get_db)):
    return controller.read_one(db, promo_code)

@router.put("/{promo_code}", response_model=schema.PromotionResponse)
def update_promotion(promo_code: str, request: schema.PromotionUpdate, db: Session = Depends(get_db)):
    return controller.update(db, promo_code, request)

@router.delete("/{promo_code}", status_code=status.HTTP_204_NO_CONTENT)
def delete_promotion(promo_code: str, db: Session = Depends(get_db)):
    return controller.delete(db, promo_code)
