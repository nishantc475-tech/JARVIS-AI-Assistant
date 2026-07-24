from listen import listen
from speak import speak
from commands import execute

speak("Jarvis is online.")

while True:

    wake = listen()

    if "hey jarvis" in wake:

        speak("Yes Nishant. How can I help you?")

        command = listen()

        if "exit" in command:
            speak("Goodbye Nishant.")
            break

        execute(command)