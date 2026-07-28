from speak import speak
from datetime import datetime

from modules.apps import handle_apps
from modules.web import handle_web
from modules.system import handle_system
from modules.media import handle_media
from modules.ai_commands import handle_ai


def execute(command):

    command = command.lower().strip()

    # Time
    if "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        return

    # Apps
    if handle_apps(command):
        return

    # Websites
    if handle_web(command):
        return

    # System
    if handle_system(command):
        return

    # Media
    if handle_media(command):
        return

    # AI
    if handle_ai(command):
        return

    speak("Sorry, I don't know how to do that yet.")