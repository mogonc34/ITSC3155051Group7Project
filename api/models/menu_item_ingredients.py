from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class MenuItemIngredient(Base):
    __tablename__ = "menu_item_ingredients"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))
    amount = Column(DECIMAL, nullable=False)