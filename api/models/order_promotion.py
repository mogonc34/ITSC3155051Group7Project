from sqlalchemy import Column, Integer, String, ForeignKey
from ..dependencies.database import Base

class OrderPromotion(Base):
    __tablename__ = 'order_promotions'
    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    promo_code = Column(String(20), ForeignKey('promotions.promo_code'), primary_key=True)
