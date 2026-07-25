import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.2)

        audio = recognizer.listen(
        source,
        timeout=5,
        phrase_time_limit=5
    )

    try:

        command = recognizer.recognize_google(audio).lower()

        print("You:", command)

        return command

    except:

        return ""