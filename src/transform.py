def clean_weather_data(data):
    return {
        'city': data.get('name'),
        'date': data.get('dt'),
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['description'] if data.get('weather') else None
    }
