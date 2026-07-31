import requests
from config import GNEWS_API_KEY


def get_news():

    url = (
        f"https://gnews.io/api/v4/top-headlines"
        f"?country=in&lang=en&max=5&apikey={GNEWS_API_KEY}"
    )

    try:

        response = requests.get(url, timeout=10)
        data = response.json()
        

        if "articles" not in data:
            return "Unable to fetch news."

        headlines = []

        for i, article in enumerate(data["articles"], start=1):
            headlines.append(f"{i}. {article['title']}")

        return "\n\n".join(headlines)

    except Exception:
        return "Unable to connect to News service."