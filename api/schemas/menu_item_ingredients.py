from pydantic import BaseModel
from typing import Optional


class MenuItemIngredientBase(BaseModel):
    menu_item_id: int
    ingredient_id: int
    amount: float


class MenuItemIngredientCreate(MenuItemIngredientBase):
    pass


class MenuItemIngredient(MenuItemIngredientBase):
    id: int

    class Config:
        from_attributes = True