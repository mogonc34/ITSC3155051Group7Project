from pydantic import ConfigDict, BaseModel
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
    model_config = ConfigDict(from_attributes=True)
