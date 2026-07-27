import requests
from config import GNEWS_API_KEY


def get_news():

    url = (
        f"https://gnews.io/api/v4/top-headlines"
        f"?country=in&lang=en&max=5&apikey={GNEWS_API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        print(data)   # Debug

        if "articles" not in data:
            return []

        headlines = []

        for article in data["articles"]:
            headlines.append(article["title"])

        return headlines

    except Exception as e:
        print(e)
        return []