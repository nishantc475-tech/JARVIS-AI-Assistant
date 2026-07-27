import requests
from config import OPENWEATHER_API_KEY


def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return "Sorry, I couldn't get the weather."

    data = response.json()

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"The weather in {city} is {desc} with a temperature of {temp} degree Celsius."