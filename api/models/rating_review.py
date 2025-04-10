from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class RatingReview(Base):
    __tablename__ = "rating_review"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rating = Column(Integer, nullable=False)
    review = Column(String(300))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
