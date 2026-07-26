from speak import speak
from ai import ask_ai
from memory import remember, recall
import webbrowser
import os
import requests
import mss
import subprocess
from datetime import datetime


def execute(command):

    command = command.lower()

    # ---------------- GOOGLE ----------------
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # ---------------- YOUTUBE ----------------
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # ---------------- CALCULATOR ----------------
    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    # ---------------- NOTEPAD ----------------
    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    # ---------------- TIME ----------------
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # ---------------- VS CODE ----------------
    elif "open vscode" in command:
        speak("Opening Visual Studio Code")
        os.system("code")

    # ---------------- WHATSAPP ----------------
    elif "open whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    # ---------------- SPOTIFY ----------------
    elif "open spotify" in command:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")

    # ---------------- GITHUB ----------------
    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    # ---------------- LINKEDIN ----------------
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    # ---------------- INSTAGRAM ----------------
    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    # ---------------- GMAIL ----------------
    elif "open gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    # ---------------- CHATGPT ----------------
    elif "open chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    # ---------------- MEMORY ----------------
    elif "remember my name is" in command:

        name = command.replace("remember my name is", "").strip()

        remember("name", name)

        speak(f"Okay, I will remember your name is {name}")

    elif "what is my name" in command:

        name = recall("name")

        if name:
            speak(f"Your name is {name}")
        else:
            speak("I don't know your name yet")

    elif "remember my favorite language is" in command:

        language = command.replace(
            "remember my favorite language is", "").strip()

        remember("language", language)

        speak(f"I will remember your favorite language is {language}")

    elif "what is my favorite language" in command:

        language = recall("language")

        if language:
            speak(f"Your favorite language is {language}")
        else:
            speak("I don't know your favorite language")

                # ---------------- GOOGLE SEARCH ----------------
    elif "search google for" in command:

        query = command.replace("search google for", "").strip()

        speak(f"Searching Google for {query}")

        webbrowser.open(
            f"https://www.google.com/search?q={query.replace(' ', '+')}"
        )

    # ---------------- YOUTUBE SEARCH ----------------
    elif "search youtube for" in command:

        query = command.replace("search youtube for", "").strip()

        speak(f"Searching YouTube for {query}")

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        )

    # ---------------- FACEBOOK ----------------
    elif "open facebook" in command:

        speak("Opening Facebook")

        webbrowser.open("https://www.facebook.com")

    # ---------------- AMAZON ----------------
    elif "open amazon" in command:

        speak("Opening Amazon")

        webbrowser.open("https://www.amazon.in")

    # ---------------- FLIPKART ----------------
    elif "open flipkart" in command:

        speak("Opening Flipkart")

        webbrowser.open("https://www.flipkart.com")

            # ---------------- SCREENSHOT ----------------
    # ---------------- SCREENSHOT ----------------
    elif "take screenshot" in command or "take a screenshot" in command:

      try:
        with mss.mss() as sct:
            filename = sct.shot(output="screenshot.png")

        speak("Screenshot saved successfully.")
        print("Saved:", filename)

      except Exception as e:
        print(e)
        speak("Sorry, I could not take the screenshot.")

    # ---------------- OPEN DOWNLOADS ----------------
    elif "open downloads" in command:

        speak("Opening Downloads folder")

        downloads = os.path.join(os.path.expanduser("~"), "Downloads")

        os.startfile(downloads)

    # ---------------- OPEN DESKTOP ----------------
    elif "open desktop" in command:

       speak("Opening Desktop")

       try:
           os.system("explorer.exe shell:desktop")
       except Exception:
           speak("Unable to open Desktop")


    # ---------------- OPEN DOCUMENTS ----------------
    elif "open documents" in command:

       speak("Opening Documents")

       try:
           os.system("explorer.exe shell:personal")
       except:
           speak("Unable to open Documents")
 
    # ---------------- OPEN D DRIVE ----------------
    elif command == "open d drive" or command == "open d":

        speak("Opening D Drive")

        os.startfile("D:\\")

    # ---------------- PLAY MUSIC ----------------
    elif "play music" in command:

        folders = [
            os.path.join(os.environ["USERPROFILE"], "Music"),
            "D:\\Music",
            "D:\\Songs",
            "D:\\Downloads"
    ]

    found = False

    for folder in folders:

        if os.path.exists(folder):

            for file in os.listdir(folder):

                if file.endswith((".mp3", ".wav")):

                    speak("Playing music")

                    os.startfile(os.path.join(folder, file))

                    found = True

                    break

        if found:
            break

    if not found:
        speak("No music file found.")

    # ---------------- OPEN ANY WEBSITE ----------------
    elif command.startswith("open "):

        website = command.replace("open ", "").strip()

        speak(f"Opening {website}")

        webbrowser.open(f"https://www.{website}.com")

    # ---------------- AI ----------------
    else:

        speak("Thinking...")

        answer = ask_ai(command)

        print("\nJarvis:", answer)

        speak(answer[:300])