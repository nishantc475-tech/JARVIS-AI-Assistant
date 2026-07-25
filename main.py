from listen import listen
from speak import speak
from commands import execute

speak("Jarvis is online.")

while True:

    command = listen()

    if not command:
        continue

    if "exit" in command:
        speak("Goodbye Nishant.")
        break

    execute(command)