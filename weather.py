import requests

url = "https://geocoding-api.open-meteo.com/v1/search?name=Sleaford&count=1"
response = requests.get(url)

geo_data = response.json()

results = geo_data["results"]
city_data = results[0]

latitude_coordinates = city_data['latitude']
longitude_coordinates = city_data['longitude']

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude_coordinates}&longitude={longitude_coordinates}&daily=temperature_2m_max,temperature_2m_min,weather_code&timezone=auto"
response = requests.get(url)

weather_data = response.json()

daily = weather_data['daily']

temperatures_min = daily['temperature_2m_min']
temperatures_max = daily['temperature_2m_max']
time = daily['time']
weather_code = daily['weather_code']

for date, low, high, code in zip(time, temperatures_min, temperatures_max, weather_code):
    print(date, low, high, code)

