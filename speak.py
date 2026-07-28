import pyttsx3

def speak(text):
    print("Jarvis:", text)

    engine = pyttsx3.init()

    engine.setProperty("rate", 180)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()