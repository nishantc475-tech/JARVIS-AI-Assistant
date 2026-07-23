import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import urllib.parse
from datetime import datetime

# Text to Speech
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

speak("Jarvis is now online.")

while True:
    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        # Open Google
        if "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # Open YouTube
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # Google Search
        elif "search" in command:
            query = command.replace("search", "").strip()

            if query:
                speak(f"Searching Google for {query}")
                url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
                webbrowser.open(url)
            else:
                speak("What should I search?")

        # Calculator
        elif "calculator" in command:
            speak("Opening Calculator")
            os.system("calc")

        # Notepad
        elif "notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        # Time
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        # Hello
        elif "hello" in command:
            speak("Hello Nishant! How can I help you?")

        # Exit
        elif "exit" in command or "stop" in command:
            speak("Goodbye Nishant!")
            break

        # Unknown Command
        else:
            speak("Sorry, I don't know this command.")

    except sr.UnknownValueError:
        print("Didn't catch that. Listening again...")

    except Exception as e:
        print("Error:", e)