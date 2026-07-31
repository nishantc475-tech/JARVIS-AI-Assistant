import requests
from config import OPENWEATHER_API_KEY


def get_weather(city):

    try:

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        )

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return "Sorry, I couldn't get the weather."

        data = response.json()

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        desc = data["weather"][0]["description"]

        return (
            f"🌦 Weather in {city}\n\n"
            f"🌡 Temperature : {temp}°C\n"
            f"🤗 Feels Like : {feels}°C\n"
            f"💧 Humidity : {humidity}%\n"
            f"💨 Wind Speed : {wind} m/s\n"
            f"☁ Condition : {desc.title()}"
        )

    except Exception:
        return "Unable to connect to the weather service."