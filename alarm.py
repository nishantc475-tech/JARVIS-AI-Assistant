import threading
import time
from datetime import datetime
from speak import speak

alarms = []


def parse_alarm_time(text):

    text = text.strip().lower()

    try:

        if "am" in text or "pm" in text:
            dt = datetime.strptime(text, "%I:%M %p")
            return dt.strftime("%H:%M")

        elif len(text.split(":")[0]) == 1:
            hour, minute = text.split(":")
            return f"0{hour}:{minute}"

        return text

    except:
        return None


def alarm_checker():

    while True:

        now = datetime.now().strftime("%H:%M")

        for alarm in alarms[:]:

            if now == alarm:

                speak("Alarm! Time is up.")

                alarms.remove(alarm)

        time.sleep(1)


def start_alarm_service():

    thread = threading.Thread(
        target=alarm_checker,
        daemon=True
    )

    thread.start()


def add_alarm(alarm_time):

    alarms.append(alarm_time)