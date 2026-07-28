import speech_recognition as sr

recognizer = sr.Recognizer()

# Better recognition settings
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        try:

            audio = recognizer.listen(
                source,
                timeout=8,
                phrase_time_limit=7
            )

            command = recognizer.recognize_google(audio)

            command = command.lower()

            print("You:", command)

            return command

        except sr.WaitTimeoutError:
            print("No voice detected.")
            return ""

        except sr.UnknownValueError:
            print("Could not understand.")
            return ""

        except sr.RequestError:
            print("Internet error.")
            return ""

        except Exception as e:
            print(e)
            return ""