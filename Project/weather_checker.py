import requests
import os
from dotenv import load_dotenv

load_dotenv()

class WeatherChecker:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.city = os.getenv("CITY")
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"

    def fetch_weather(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        return None

    def get_alert_message(self, data):
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['main'].lower()
        wind_speed = data['wind']['speed']
        
        # Logic for conditions
        if "rain" in weather_desc:
            return "🌧️ Carry an umbrella! Rain is detected."
        elif temp >= 38:
            return f"🔥 Extreme heat warning! It's {temp}°C."
        elif wind_speed >= 15:
            return "💨 Strong wind warning! Stay safe."
        # Add more conditions here...
        
        return None # No alert needed
