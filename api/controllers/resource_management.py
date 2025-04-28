from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import resource_management as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_resource = model.ResourceManagement(
        ingredient=request.ingredient,
        amount = request.amount,
        unit = request.unit
    )

    try:
        db.add(new_resource)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_resource

def read_all(db: Session):
    try:
        result = db.query(model.ResourceManagement).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def read_one(db: Session, new_resource):
    try:
        item = db.query(model.ResourceManagement).filter(model.ResourceManagement.id == new_resource).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

def update(db: Session, new_resource, request):
    try:
        item = db.query(model.ResourceManagement).filter(model.ResourceManagement.id == new_resource).first()
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, new_resource):
    try:
        item = db.query(model.ResourceManagement).filter(model.ResourceManagement.id == new_resource)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)