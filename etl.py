from src.extract import fetch_weather
from src.transform import clean_weather_data
from src.load import load_multiple_times

def fetch_and_clean_for_city(city):
    raw_data = fetch_weather(city)
    return clean_weather_data(raw_data)

if __name__ == "__main__":
    cities = ['London', 'New York', 'Tokyo', 'Paris', 'Sydney']
    for city in cities:
        print(f"Starting data collection for {city}")
        load_multiple_times(lambda: fetch_and_clean_for_city(city))
        print(f"Weather data for {city} loaded to database.")
