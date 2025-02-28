from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, help_api
from app.database import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows CORS for your specified origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/locations", response_model=list[schemas.LocationOut])
def read_locations(db: Session = Depends(get_db)):
    """
    Retrieve a list of all locations saved in the database,
    including their current weather conditions from OpenMeteo API.
    """
    locations = crud.get_locations(db)
    for location in locations:
        weather = help_api.get_current_weather(location.latitude, location.longitude)
        if weather:
            location.weather = {
                "temperature": weather["temperature"],
                "min_temperature": weather["min_temperature"],
                "max_temperature": weather["max_temperature"],
                "rainfall": weather["rainfall"],
                "weather": weather["weather"],
            }
    return locations

@app.post("/locations", response_model=schemas.LocationOut)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    """
    Add a new location with name, latitude, and longitude.
    If latitude and longitude are missing, fetch them using geolocation API.
    """
    if location.latitude is None or location.longitude is None:
        coordinates = help_api.get_lat_lon(location.name)
        if coordinates:
            location.latitude, location.longitude = coordinates
        else:
            raise HTTPException(status_code=400, detail="Invalid city name. Could not find coordinates.")

    return crud.create_location(db, location)

@app.delete("/locations/{location_id}")
def delete_location(location_id: int, db: Session = Depends(get_db)):
    """
    Delete a location by its ID.
    """
    location = crud.delete_location(db, location_id)
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return {"message": "Location deleted successfully"}


@app.get("/forecast/{location_id}", response_model=schemas.WeatherForecast)
def get_weather_forecast(location_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a 7-day weather forecast for a specified location by its ID.
    """
    # Use the updated function to retrieve the location
    location = crud.get_location_by_id(db, location_id)
    
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")

    # Fetch the 7-day weather forecast using the location's coordinates
    print(location.latitude, location.longitude)
    forecast = help_api.get_weather_forecast(location.latitude, location.longitude)
    print(forecast)
    return forecast
