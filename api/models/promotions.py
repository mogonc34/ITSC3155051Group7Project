from sqlalchemy import Column, String, Text, DECIMAL, Date, CheckConstraint
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = 'promotions'

    promo_code = Column(String(20), primary_key=True)
    description = Column(Text)
    discount_percent = Column(DECIMAL(5, 2), nullable=False)
    expiration_date = Column(Date)

    __table_args__ = (
        CheckConstraint('discount_percent >= 0 AND discount_percent <= 100', name='check_discount_percent_range'),
    )
