from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    calories: Optional[int] = None
    food_category: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None

class MenuItemResponse(MenuItemBase):
    menu_item_id: int

    class Config:
        orm_mode = True
