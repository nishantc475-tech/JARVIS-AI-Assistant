import speech_recognition as sr
import pyttsx3
import os

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    speak("I am listening")
    print("Listening...")
    r.adjust_for_ambient_noise(source)

    audio = r.listen(source)

try:
    command = r.recognize_google(audio).lower()
    print("You said:", command)

    if "google" in command:
        speak("Opening Google")
        os.system("start https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        os.system("start https://www.youtube.com")

    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    else:
        speak("Sorry, I don't know this command.")

except Exception:
    speak("Sorry, I could not understand.")