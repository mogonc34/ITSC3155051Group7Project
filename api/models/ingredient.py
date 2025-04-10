from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base

class Ingredient(Base):
    __tablename__ = 'ingredients'
    ingredient_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    unit = Column(String(20))
    quantity_available = Column(DECIMAL(10, 2))
