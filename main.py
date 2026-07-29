import time
import random

from listen import listen
from speak import speak
from commands import execute
from alarm import start_alarm_service

WAKE_WORDS = [
    "jarvis",
    "jarv",
    "hey jarvis",
    "hey jarv",
    "jar"
]

GREETINGS = [
    "Yes Nishant, how can I help?",
    "I'm listening.",
    "Go ahead.",
    "What can I do for you?",
    "Hello Nishant.",
    "Tell me your command.",
    "Yes?",
    "Ready."
]

speak("Jarvis is online.")
start_alarm_service()

while True:

    print("🎤 Waiting for wake word...")

    wake = listen()

    if wake == "":
        continue

    wake = wake.lower().strip()

    if "exit" in wake:
        speak("Goodbye Nishant.")
        break

    if wake in WAKE_WORDS:

        speak(random.choice(GREETINGS))   # Baad me random karenge

        last_activity = time.time()

        while True:

            # 30 second inactivity
            if time.time() - last_activity > 30:
                speak("No activity detected. Going to sleep.")
                break

            print("🎤 Listening for command...")

            command = listen()

            if command == "":
                continue

            last_activity = time.time()

            command = command.lower().strip()

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