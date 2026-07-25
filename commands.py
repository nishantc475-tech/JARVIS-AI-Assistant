from speak import speak
from ai import ask_ai
import webbrowser
import os
from datetime import datetime

def execute(command):

    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    else:
        speak("Thinking...")
        answer = ask_ai(command)

        short_answer = answer[:250]

        print(short_answer)
        speak(short_answer)
     