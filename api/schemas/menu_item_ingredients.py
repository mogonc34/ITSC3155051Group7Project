from pydantic import BaseModel
from decimal import Decimal

class MenuItemIngredientBase(BaseModel):
    menu_item_id: int
    ingredient_id: int
    quantity_required: Decimal

class MenuItemIngredientCreate(MenuItemIngredientBase):
    pass

class MenuItemIngredientUpdate(BaseModel):
    quantity_required: Decimal

class MenuItemIngredient(MenuItemIngredientBase):
    class Config:
        from_attributes = True
