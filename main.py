import speech_recognition as sr
import pyttsx3
import os

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

        elif "time" in command:
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif "exit" in command or "stop" in command:
            speak("Goodbye Nishant!")
            break

        else:
            speak("Sorry, I don't know that command.")

    except Exception:
        print("Didn't catch that. Listening again...")