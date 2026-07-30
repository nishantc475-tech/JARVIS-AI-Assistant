import threading
import time
from datetime import datetime

from scheduler import get_schedule, remove_schedule
from speak import speak

# Already triggered reminders (same session)
triggered = set()


def reminder_checker():

    while True:

        current_time = datetime.now().strftime("%I:%M %p").lstrip("0")

        tasks = get_schedule()

        for task in tasks:

            task_name = task["task"].strip()
            task_time = task["time"].strip()

            unique = f"{task_name}_{task_time}"

            if task_time == current_time and unique not in triggered:

                speak(f"Nishant, it's time for {task_name}")

                print(f"Reminder: {task_name}")

                triggered.add(unique)

                # Remove completed reminder
                remove_schedule(task_name, task_time)

                print(f"Completed: {task_name}")

        time.sleep(20)


def start_reminder_engine():

    thread = threading.Thread(
        target=reminder_checker,
        daemon=True
    )

    thread.start()