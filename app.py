from flask import Flask,render_template, request
import requests

app = Flask(__name__)

WEATHER_CODES_DICT = {
    0:"Clear Sky",
    1:"Mainly clear",
    2:"Partly cloudy",
    3:"Overcast",
    45:"Fog",
    48:"Depositing rime fog",
    51:"Drizzle - Light",
    53:"Drizzle - Moderate",
    55:"Drizzle - Dense",
    56:"Freezing Drizzle - Light and dense intensity",
    57:"Freezing Drizzle - Dense intensity",
    61:"Rain - Slight",
    63:"Rain - Moderate",
    65:"Rain - Heavy",
    66:"Freezing Rain - Light",
    67:"Freezing Rain:Heavy",
    71:"Snow fall - Light",
    73:"Snow fall- Moderate",
    75:"Snow fall - Heavy",
    77:"Snow grains",
    80:"Rain Showers - Slight",
    81:"Rain Showers - Moderate",
    82:"Rain Showers - Violent",
    85:"Snow Showers - Slight",
    86:"Snow Showers - Heavy",
    95:"Thunderstorm - Slight/Moderate",
    96:"Thunderstorm - Slight Hail",
    99:"Thunderstorm - Heavy Hail"
}

def get_coordinates(cityname):
    
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={cityname}&count=1"
    geocode_response = requests.get(geocode_url)
    geocode_data = geocode_response.json()
    
    
    location = geocode_data["results"][0]
    latitude = location["latitude"]
    longitude = location["longitude"]
    return latitude, longitude


def get_forecast(latitude, longitude):
    
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,weather_code&timezone=auto"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    daily_data = weather_data['daily']

    dates = daily_data["time"]
    temp_min = daily_data["temperature_2m_min"]
    temp_max = daily_data["temperature_2m_max"]
    weather_codes = daily_data["weather_code"]

    return dates, temp_min, temp_max, weather_codes


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form["city"]
        latitude, longitude = get_coordinates(city)
        dates, temp_min, temp_max, weather_codes = get_forecast(latitude, longitude)
        return render_template("index.html", dates=dates, temp_min=temp_min, temp_max=temp_max, weather_codes=weather_codes, weather_codes_dict = WEATHER_CODES_DICT, city=city)
    
    return render_template("index.html")


app.run(debug=True)