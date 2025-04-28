from pydantic import BaseModel
from typing import Optional

class IngredientBase(BaseModel):
    name: str
    unit: Optional[str] = None
    quantity_available: Optional[float] = None

class IngredientCreate(IngredientBase):
    pass

class IngredientUpdate(BaseModel):
    name: Optional[str] = None
    unit: Optional[str] = None
    quantity_available: Optional[float] = None

class IngredientResponse(IngredientBase):
    ingredient_id: int

    class Config:
        from_attributes = True
