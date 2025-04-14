from pydantic import BaseModel, EmailStr
from typing import Optional, List

class MenuItemBase(BaseModel):
    name: str
    description: Optional[str]
    price: float
    calories: Optional[int]
    food_category: Optional[str]

class MenuItemResponse(MenuItemBase):
    menu_item_id: int

    class Config:
        from_attributes = True
