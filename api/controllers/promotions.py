from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models import promotions as model
from ..schemas import promotions as schema


def create(db: Session, request: schema.PromotionCreate):
    new_promo = model.Promotion(
        promotion_name=request.promotion_name,
        promotion_description=request.promotion_description,
        promotion_end_date=request.promotion_end_date,
        promotion_start_date=request.promotion_start_date
    )

    try:
        db.add(new_promo)
        db.commit()
        db.refresh(new_promo)
        return new_promo
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_all(db: Session):
    try:
        return db.query(model.Promotion).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_one(db: Session, promo_id: int):
    try:
        promo = db.query(model.Promotion).filter(model.Promotion.id == promo_id).first()
        if not promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found!")
        return promo
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def update(db: Session, promo_id: int, request: schema.PromotionUpdate):
    try:
        promo_query = db.query(model.Promotion).filter(model.Promotion.id == promo_id)
        promo = promo_query.first()

        if not promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found!")

        update_data = request.dict(exclude_unset=True)
        promo_query.update(update_data, synchronize_session=False)
        db.commit()
        return promo_query.first()
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def delete(db: Session, promo_id: int):
    try:
        promo = db.query(model.Promotion).filter(model.Promotion.id == promo_id)
        if not promo.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Promotion ID not found!")
        promo.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

# The 66-lines of code below this line are the original skeleton code provided by @samfallahian for the course project
# from sqlalchemy.orm import Session
# from fastapi import HTTPException, status, Response, Depends
# from ..models import promotions as model
# from sqlalchemy.exc import SQLAlchemyError
#
# def create(db: Session, request):
#     new_item = model.Promotion(
#         promotion_name=request.promotion_name,
#         promotion_description = request.promotion_description,
#         promotion_start_date = request.promotion_start_date,
#         promotion_end_date = request.promotion_end_date
#     )
#
#     try:
#         db.add(new_item)
#         db.commit()
#         db.refresh(new_item)
#     except SQLAlchemyError as e:
#         error = str(e.__dict__['orig'])
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
#     return new_item
#
# def read_all(db: Session):
#     try:
#         result = db.query(model.Promotion).all()
#     except SQLAlchemyError as e:
#         error = str(e.__dict__['orig'])
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
#     return result
#
# def read_one(db: Session, item_id):
#     try:
#         item = db.query(model.Promotion).filter(model.Promotion.id == item_id).first()
#         if not item:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
#     except SQLAlchemyError as e:
#         error = str(e.__dict__['orig'])
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
#     return item
#
# def update(db: Session, item_id, request):
#     try:
#         item = db.query(model.Promotion).filter(model.Promotion.id == item_id)
#         if not item.first():
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
#         update_data = request.dict(exclude_unset=True)
#         item.update(update_data, synchronize_session=False)
#         db.commit()
#     except SQLAlchemyError as e:
#         error = str(e.__dict__['orig'])
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
#     return item.first()
#
#
# def delete(db: Session, item_id):
#     try:
#         item = db.query(model.Promotion).filter(model.Promotion.id == item_id)
#         if not item.first():
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
#         item.delete(synchronize_session=False)
#         db.commit()
#     except SQLAlchemyError as e:
#         error = str(e.__dict__['orig'])
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
