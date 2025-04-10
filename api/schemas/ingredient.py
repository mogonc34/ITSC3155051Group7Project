from pydantic import BaseModel
from typing import Optional

class IngredientBase(BaseModel):
    name: str
    unit: Optional[str]
    quantity_available: float

class IngredientResponse(IngredientBase):
    ingredient_id: int

    class Config:
        orm_mode = True
