import sqlite3

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
