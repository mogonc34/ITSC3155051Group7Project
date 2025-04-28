from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from ..dependencies.database import Base

class MenuItemIngredient(Base):
    __tablename__ = "menu_item_ingredients"

    menu_item_id = Column(Integer, ForeignKey("menu_items.menu_item_id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.ingredient_id"), primary_key=True)
    quantity_required = Column(DECIMAL(10, 2), nullable=False)
