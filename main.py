from listen import listen
from speak import speak
from commands import execute

WAKE_WORDS = ["jarv","hey jarv","hey jarvis","jar","hello", "jarvis"]

speak("Jarvis is online.")

while True:

    print("🎤 Waiting for wake word...")

    wake = listen()

    if wake == "":
        continue

    wake = wake.lower()

    if "exit" in wake:
        speak("Goodbye Nishant.")
        break

    if wake.strip() in WAKE_WORDS:

        speak("I'm listening.")

        while True:

            print("🎤 Listening for command...")

            command = listen()

            if command == "":
                continue

            command = command.lower()

            if "exit" in command:
                speak("Goodbye Nishant.")
                exit()

            if (
                "sleep" in command
                or "go to sleep" in command
                or "stop listening" in command
            ):
                speak("Going to sleep.")
                break

            execute(command)