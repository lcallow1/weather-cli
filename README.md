# Weather App

A weather project built in two stages as a learning exercise — first as a CLI tool, then as a web dashboard.

## CLI Version (`weather.py`)

Run directly in the terminal:
- Takes any city as user input
- Fetches a 7-day forecast from the Open-Meteo API
- Displays formatted output with weather descriptions, min and max temps

## Web Dashboard (`app.py`)

A Flask web app built on top of the same logic:
- Search for any city via a web interface
- Displays a 7-day forecast as a clean card-based dashboard

## Built with

- Python 3
- Flask
- requests
- Open-Meteo API

## Running the web app

```bash
pip install flask requests
python app.py
```

Then visit `http://127.0.0.1:5000` in your browser.