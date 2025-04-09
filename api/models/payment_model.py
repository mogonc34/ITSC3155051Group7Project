from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base  # Assuming you have Base from your DB setup

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)

    payment_type = Column(String, nullable=False)         # e.g., credit, debit, paypal
    card_number = Column(String, nullable=False)
    transaction_status = Column(String, default="pending") # success, failed, etc.
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)

    order = relationship("Order", back_populates="payment")
