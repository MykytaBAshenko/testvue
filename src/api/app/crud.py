from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(**location.dict())
    db.add(db_location)
    
    try:
        db.commit()
        db.refresh(db_location)
        return db_location
    except IntegrityError:
        db.rollback()  # Rollback to avoid partial commit
        raise HTTPException(status_code=400, detail="Location with this name already exists.")

# Retrieve all locations
def get_locations(db: Session):
    return db.query(models.Location).all()

# Delete a location by ID
def delete_location(db: Session, location_id: int):
    location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if location:
        db.delete(location)
        db.commit()
    return location

def get_location_by_id(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.id == location_id).first()
