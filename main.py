import time
import random

from listen import listen
from speak import speak
from commands import execute
from alarm import start_alarm_service
from logger import log
from reminder_engine import start_reminder_engine
from context import set_last_command

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
log("Jarvis started.")

start_alarm_service()
start_reminder_engine()

while True:

    print("🎤 Waiting for wake word...")

    wake = listen()

    if wake == "":
        continue

    wake = wake.lower().strip()

    if "exit" in wake:
        speak("Goodbye Nishant.")
        log("Jarvis closed.")
        break

    if wake in WAKE_WORDS:

        log(f"Wake word detected: {wake}")

        speak(random.choice(GREETINGS))

        last_activity = time.time()

        while True:

            # Auto sleep after 30 seconds
            if time.time() - last_activity > 30:
                log("Sleep mode due to inactivity.")
                speak("No activity detected. Going to sleep.")
                break

            print("🎤 Listening for command...")

            command = listen()

            if command == "":
                continue

            last_activity = time.time()

            command = command.lower().strip()

            log(f"User: {command}")
            set_last_command(command)

            if "exit" in command:
                speak("Goodbye Nishant.")
                log("Jarvis closed.")
                exit()

            if (
                "sleep" in command
                or "go to sleep" in command
                or "stop listening" in command
            ):
                log("Jarvis entered sleep mode.")
                speak("Going to sleep.")
                break

            execute(command)