from src.extract import fetch_weather
from src.transform import clean_weather_data
from src.load import load_to_db

if __name__ == "__main__":
    city = 'London'
    raw_data = fetch_weather(city)
    cleaned = clean_weather_data(raw_data)
    load_to_db(cleaned)
    print(f"Weather data for {city} loaded to database.")
