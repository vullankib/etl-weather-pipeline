import requests
from src.config import get_api_key

def fetch_weather(city):
    api_key = get_api_key()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
