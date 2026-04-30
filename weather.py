import requests

geocode_url = "https://geocoding-api.open-meteo.com/v1/search?name=Sleaford&count=1"
geocode_response = requests.get(geocode_url)
geocode_data = geocode_response.json()

location = geocode_data["results"][0]
latitude = location["latitude"]
longitude = location["longitude"]


weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,weather_code&timezone=auto"
weather_response = requests.get(weather_url)

weather_data = weather_response.json()

daily_data = weather_data['daily']

dates = daily_data["time"]
temp_min = daily_data["temperature_2m_min"]
temp_max = daily_data["temperature_2m_max"]
weather_codes = daily_data["weather_code"]


for date, low, high, code in zip(dates, temp_min, temp_max, weather_codes):
    print(date, low, high, code)

