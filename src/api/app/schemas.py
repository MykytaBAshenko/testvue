from pydantic import BaseModel, Field
from typing import Optional, List

class LocationBase(BaseModel):
    name: str
    latitude: Optional[float] = Field(default=None, description="Latitude of the location")
    longitude: Optional[float] = Field(default=None, description="Longitude of the location")

class LocationCreate(LocationBase):
    pass


class WeatherOut(BaseModel):
    temperature: float
    min_temperature: float
    max_temperature: float
    rainfall: float
    weather: int


class LocationOut(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    weather: Optional[WeatherOut] = None 

class WeatherForecast(BaseModel):
    time: List[str]
    temperature_2m_min: List[float]
    temperature_2m_max: List[float]
    weathercode: List[int]
