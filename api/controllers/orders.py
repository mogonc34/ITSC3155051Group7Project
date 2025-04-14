# from sqlalchemy.orm import Session
# from fastapi import HTTPException, status, Response
# from sqlalchemy.exc import SQLAlchemyError
# from datetime import datetime
# import uuid
#
# from .. import models  # assuming your SQLAlchemy models are in api/models
# from ..schemas import order as order_schema
# from ..schemas.order import OrderDetailCreate
#
#
# def generate_tracking_number():
#     return str(uuid.uuid4()).replace("-", "")[:12]
#
#
# def calculate_total_price(order_details: list[OrderDetailCreate]) -> float:
#     return sum(detail.quantity * detail.unit_price for detail in order_details)
#
#
# def create(db: Session, request: order_schema.OrderCreate):
#     tracking_number = generate_tracking_number()
#     total_price = calculate_total_price(request.order_details)
#
#     new_order = models.order.Order(
#         customer_id=request.customer_id,
#         tracking_number=tracking_number,
#         order_date=datetime.utcnow(),
#         total_price=total_price
#     )
#
#     try:
#         db.add(new_order)
#         db.flush()  # To get new_order.id before adding order details
#
#         # Add related order details
#         for detail in request.order_details:
#             new_detail = models.order.OrderDetail(
#                 order_id=new_order.id,
#                 product_id=detail.product_id,
#                 quantity=detail.quantity,
#                 unit_price=detail.unit_price
#             )
#             db.add(new_detail)
#
#         db.commit()
#         db.refresh(new_order)
#     except SQLAlchemyError as e:
#         db.rollback()
#         error = str(e.__dict__['orig'])
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
#
#     return new_order
#
#
# def read_all(db: Session):
#     try:
#         return db.query(models.order.Order).all()
#     except SQLAlchemyError as e:
#         error = str(e.__dict__['orig'])
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
#
#
# def read_one(db: Session, item_id: int):
#     try:
#         item = db.query(models.order.Order).filter(models.order.Order.id == item_id).first()
#         if not item:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order ID not found!")
#         return item
#     except SQLAlchemyError as e:
#         error = str(e.__dict__['orig'])
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
#
#
# def update(db: Session, item_id: int, request: order_schema.OrderUpdate):
#     try:
#         item_query = db.query(models.order.Order).filter(models.order.Order.id == item_id)
#         order = item_query.first()
#
#         if not order:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order ID not found!")
#
#         update_data = request.dict(exclude_unset=True)
#
#         item_query.update(update_data, synchronize_session=False)
#         db.commit()
#         return item_query.first()
#
#     except SQLAlchemyError as e:
#         db.rollback()
#         error = str(e.__dict__['orig'])
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
#
#
# def delete(db: Session, item_id: int):
#     try:
#         item = db.query(models.order.Order).filter(models.order.Order.id == item_id)
#         if not item.first():
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order ID not found!")
#         item.delete(synchronize_session=False)
#         db.commit()
#         return Response(status_code=status.HTTP_204_NO_CONTENT)
#     except SQLAlchemyError as e:
#         db.rollback()
#         error = str(e.__dict__['orig'])
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
