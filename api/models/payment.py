from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = 'payments'

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable=False)
    payment_type = Column(String(50))
    card_last_four = Column(String(4))
    transaction_status = Column(String(50))
    transaction_date = Column(TIMESTAMP, server_default=func.now())
