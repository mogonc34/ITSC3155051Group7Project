from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ..schemas import ingredient as schema
from ..controllers import ingredient as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/ingredients",
    tags=["Ingredients"]
)

@router.post("/", response_model=schema.IngredientResponse, status_code=status.HTTP_201_CREATED)
def create_ingredient(request: schema.IngredientCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.IngredientResponse])
def get_all_ingredients(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{ingredient_id}", response_model=schema.IngredientResponse)
def get_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, ingredient_id)

@router.put("/{ingredient_id}", response_model=schema.IngredientResponse)
def update_ingredient(ingredient_id: int, request: schema.IngredientUpdate, db: Session = Depends(get_db)):
    return controller.update(db, ingredient_id, request)

@router.delete("/{ingredient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, ingredient_id)
