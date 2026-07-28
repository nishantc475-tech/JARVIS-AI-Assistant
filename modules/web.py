import webbrowser
from speak import speak


def handle_web(command):

    # Open Websites
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "gmail": "https://mail.google.com",
        "chatgpt": "https://chatgpt.com",
        "instagram": "https://instagram.com",
        "facebook": "https://facebook.com",
        "amazon": "https://amazon.in",
        "flipkart": "https://flipkart.com",
        "linkedin": "https://linkedin.com",
        "spotify": "https://open.spotify.com",
        "whatsapp": "https://web.whatsapp.com",
    }

    for name, url in websites.items():
        if f"open {name}" in command:
            speak(f"Opening {name}")
            webbrowser.open(url)
            return True

    # Google Search
    if "search google for" in command:

        query = command.replace("search google for", "").strip()

        speak(f"Searching Google for {query}")

        webbrowser.open(
            f"https://www.google.com/search?q={query.replace(' ', '+')}"
        )

        return True

    # YouTube Search
    if "search youtube for" in command:

        query = command.replace("search youtube for", "").strip()

        speak(f"Searching YouTube for {query}")

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        )

        return True

    return False