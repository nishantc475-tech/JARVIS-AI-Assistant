import speech_recognition as sr
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Listening...")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

try:
    command = r.recognize_google(audio).lower()
    print("You said:", command)

    if "hello" in command or "jarv" in command:
       print("Hello Nishant! How can I help you?")
       
    elif "google" in command:
       print("Opening Google...")
       os.system("start https://www.google.com")

    elif "notepad" in command:
       print("Opening Notepad...")
       os.system("notepad")

    elif "calculator" in command:
       print("Opening Calculator...")
       os.system("calc")

    else:
       print("Command not recognized.")
  

except Exception as e:
    print("Error:", e)