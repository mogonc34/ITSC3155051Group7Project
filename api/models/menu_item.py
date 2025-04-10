from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey, Date, TIMESTAMP
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'
    menu_item_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    calories = Column(Integer)
    food_category = Column(String(50))