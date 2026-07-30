import webbrowser
import subprocess
import urllib.parse


def run_automation(command):

    command = command.lower()

    # YouTube Search
    if "open youtube and search" in command:

        query = command.replace(
            "open youtube and search",
            ""
        ).strip()

        url = (
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return True

    # Google Search
    if "open google and search" in command:

        query = command.replace(
            "open google and search",
            ""
        ).strip()

        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return True

    # Calculator + Chrome
    if "open calculator and chrome" in command:

        subprocess.Popen("calc.exe")

        webbrowser.open("https://google.com")

        return True

    return False