from weather_checker import WeatherChecker
from notifier import EmailNotifier

def main():
    checker = WeatherChecker()
    notifier = EmailNotifier()

    print("Fetching weather data...")
    weather_data = checker.fetch_weather()

    if weather_data:
        alert = checker.get_alert_message(weather_data)
        if alert:
            print(f"Alert triggered: {alert}")
            notifier.send_alert(" Weather Alert!", alert)
        else:
            print(" Weather is fine. No alert needed.")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()