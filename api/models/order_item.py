from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey, Date, TIMESTAMP
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderItem(Base):
    __tablename__ = 'order_items'
    order_item_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'), nullable=False)
    menu_item_id = Column(Integer, ForeignKey('menu_items.menu_item_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    item_price = Column(DECIMAL(10, 2), nullable=False)