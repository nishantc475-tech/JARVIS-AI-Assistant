from listen import listen
from speak import speak
from commands import execute

speak("Jarvis is online.")

while True:
    command = listen()

    if not command:
        continue

    # Exit
    if "exit" in command or "stop" in command:
        speak("Goodbye Nishant.")
        break

    # Wake Word
    if "hey jarvis" in command:
        speak("Yes Nishant. How can I help you?")
        command = listen()

        if command:
            execute(command)

    else:
        print("Waiting for wake word...")