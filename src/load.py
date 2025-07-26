import sqlite3
import time

def load_to_db(cleaned_data, db_path='data/weather.db'):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather (
        city TEXT,
        date INTEGER,
        temperature REAL,
        humidity INTEGER,
        weather TEXT
    )''')
    c.execute('''INSERT INTO weather (city, date, temperature, humidity, weather)
                 VALUES (?, ?, ?, ?, ?)''',
              (cleaned_data['city'], cleaned_data['date'], cleaned_data['temperature'], cleaned_data['humidity'], cleaned_data['weather']))
    conn.commit()
    conn.close()

# New function to run loading every minute for 10 times
def load_multiple_times(fetch_and_clean_func, db_path='data/weather.db', times=10, interval=60):
    for i in range(times):
        cleaned_data = fetch_and_clean_func()
        load_to_db(cleaned_data, db_path)
        print(f"Loaded data iteration {i+1}")
        if i < times - 1:
            time.sleep(interval)
