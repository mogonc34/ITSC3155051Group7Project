from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_name = Column(String(100))
    promotion_description = Column(String(300))
    promotion_start_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    promotion_end_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))