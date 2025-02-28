import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

def get_lat_lon(city_name):
    """
    Get latitude and longitude for a given city name.
    Returns None if the city does not exist or cannot be found.
    """
    try:
        geolocator = Nominatim(user_agent="city_geocoder")
        location = geolocator.geocode(city_name)
        if location:
            return location.latitude, location.longitude
    except (GeocoderTimedOut, GeocoderServiceError):
        return None
    return None

def get_current_weather(latitude: float, longitude: float):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current_weather=true"
        f"&daily=temperature_2m_min,temperature_2m_max,precipitation_sum"
        f"&timezone=auto"
    )
    response = requests.get(url)
    if response.ok:
        data = response.json()
        return {
            "temperature": data["current_weather"]["temperature"],
            "min_temperature": data["daily"]["temperature_2m_min"][0],
            "max_temperature": data["daily"]["temperature_2m_max"][0],
            "rainfall": data["daily"]["precipitation_sum"][0],
            "weather": data["current_weather"]["weathercode"]
        }
    return None


def get_weather_forecast(latitude: float, longitude: float):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&daily=temperature_2m_min,temperature_2m_max,precipitation_sum,weathercode"
        f"&timezone=auto"
    )
    response = requests.get(url)
    if response.ok:
        data = response.json()
        print(data)  # Inspect the full response to check the structure

        time = data["daily"]["time"]
        temperature_2m_min = data["daily"]["temperature_2m_min"]
        temperature_2m_max = data["daily"]["temperature_2m_max"]
        weathercode = data["daily"]["weathercode"]
        
        return {
            "time": time,
            "temperature_2m_min": temperature_2m_min,
            "temperature_2m_max": temperature_2m_max,
            "weathercode": weathercode
        }
    return None