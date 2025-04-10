from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey, Date, TIMESTAMP
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20))
    address = Column(Text)