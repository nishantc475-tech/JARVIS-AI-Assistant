import psutil
import requests
from datetime import datetime
from speak import speak


def handle_system(command):

    # Battery
    if "battery" in command:

        battery = psutil.sensors_battery()

        if battery:

            percent = battery.percent
            status = "charging" if battery.power_plugged else "not charging"

            message = f"Battery is {percent} percent and {status}."

            print(message)
            speak(message)

        else:
            speak("Battery information is not available.")

        return True

    # CPU
    elif "cpu" in command:

        cpu = psutil.cpu_percent(interval=1)

        message = f"CPU usage is {cpu} percent."

        print(message)
        speak(message)

        return True

    # RAM
    elif "ram" in command or "memory usage" in command:

        memory = psutil.virtual_memory()

        used = round(memory.used / (1024 ** 3), 2)
        total = round(memory.total / (1024 ** 3), 2)

        message = (
            f"RAM usage is {memory.percent} percent. "
            f"{used} GB used out of {total} GB."
        )

        print(message)
        speak(message)

        return True

    # Date
    elif "date" in command:

        today = datetime.now().strftime("%d %B %Y")

        message = f"Today's date is {today}."

        print(message)
        speak(message)

        return True

    # Day
    elif "day" in command:

        current_day = datetime.now().strftime("%A")

        message = f"Today is {current_day}."

        print(message)
        speak(message)

        return True

    # Storage
    elif "storage" in command or "disk" in command:

        disk = psutil.disk_usage("C:\\")

        total = round(disk.total / (1024 ** 3), 2)
        used = round(disk.used / (1024 ** 3), 2)
        free = round(disk.free / (1024 ** 3), 2)

        message = (
            f"C drive storage: {used} GB used, "
            f"{free} GB free, out of {total} GB."
        )

        print(message)
        speak(message)

        return True

    # Public IP
    elif "ip address" in command or "my ip" in command:

        try:

            ip = requests.get("https://api.ipify.org").text

            message = f"Your public IP address is {ip}"

            print(message)
            speak(message)

        except Exception:

            speak("Sorry, I could not get your IP address.")

        return True

    return False