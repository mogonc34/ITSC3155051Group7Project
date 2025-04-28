from sqlalchemy import Column, Integer, Text, ForeignKey, SmallInteger, CheckConstraint
from ..dependencies.database import Base

class RatingReview(Base):
    __tablename__ = 'ratings_reviews'

    review_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable=False)
    menu_item_id = Column(Integer, ForeignKey('menu_items.menu_item_id'), nullable=False)
    review_text = Column(Text)
    score = Column(SmallInteger, nullable=False)

    __table_args__ = (
        CheckConstraint('score BETWEEN 1 AND 5', name='check_score_range'),
    )
