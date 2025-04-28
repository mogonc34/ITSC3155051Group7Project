from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class ResourceManagement(Base):
    __tablename__ = 'resource_management'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ingredient = Column(String(300), nullable=False)
    amount = Column(Integer, nullable=False)
    unit = Column(Integer, nullable=False)