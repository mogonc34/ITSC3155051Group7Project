from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable=False)
    payment_id = Column(Integer, ForeignKey('payments.payment_id'))
    order_date = Column(TIMESTAMP, server_default=func.now())
    order_status = Column(String(50))
    total_price = Column(DECIMAL(10, 2))
