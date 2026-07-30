from speak import speak
from ai import ask_ai
from memory import remember, recall
from weather import get_weather
from news import get_news
from todo import add_task, show_tasks, clear_tasks
from reminder import (
    add_reminder,
    show_reminders,
    clear_reminders,
)
from alarm import add_alarm, parse_alarm_time
from system_info import cpu_usage, ram_usage, battery, disk_usage
from clipboard import get_clipboard
from vision import describe_screen
from camera import open_camera
from camera import take_photo
from pdf_reader import choose_pdf, summarize_pdf
from ocr import read_image_text
from file_search import find_file
import os
from internet_speed import check_speed
from voice_notes import record_voice, play_voice

def handle_ai(command):

    command = command.lower().strip()
     # Greetings
    if command in ["hi", "hello", "hey"]:
        speak("Hello Nishant. Nice to see you.")
        return True
    
    if "good morning" in command:
        speak("Good morning Nishant. Hope you have a wonderful day.")
        return True
    
    if "good night" in command:
        speak("Good night Nishant. Sweet dreams.")
        return True
    
    if "thank you" in command or "thanks" in command:
        speak("You're welcome Nishant.")
        return True
    
    if "how are you" in command:
        speak("I'm doing great. Thank you for asking.")
        return True
    
    if "who are you" in command:
        speak("I'm Jarvis, your personal AI Assistant.")
        return True
    
    if "who made you" in command:
        speak("I was created by Nishant using Python and Gemini AI.")
        return True
    
    if "i love you" in command:
        speak("Thank you Nishant. I'm always here to help you.")
        return True
    
    # ---------------- WEATHER ----------------
    if "weather" in command:

        city = "Dehradun"

        if "in " in command:
            city = command.split("in ", 1)[1].strip()

        result = get_weather(city)

        print(result)

        speak(result)

        return True

    # ---------------- NEWS ----------------
    elif "news" in command or "headlines" in command:

        speak("Here are today's top headlines.")

        headlines = get_news()

        if headlines:

            for i, headline in enumerate(headlines, start=1):
                print(f"{i}. {headline}")
                speak(headline)

        else:

            speak("Sorry, I could not fetch the news.")

        return True

    # ---------------- MEMORY : NAME ----------------
    elif "remember my name is" in command:

        name = command.replace("remember my name is", "").strip()

        remember("name", name)

        speak(f"Okay, I will remember your name is {name}")

        return True

    elif "what is my name" in command:

        name = recall("name")

        if name:
            speak(f"Your name is {name}")
        else:
            speak("I don't know your name yet")

        return True

    # ---------------- MEMORY : LANGUAGE ----------------
    elif "remember my favorite language is" in command:

        language = command.replace(
            "remember my favorite language is", ""
        ).strip()

        remember("language", language)

        speak(f"I will remember your favorite language is {language}")

        return True

    elif "what is my favorite language" in command:

        language = recall("language")

        if language:
            speak(f"Your favorite language is {language}")
        else:
            speak("I don't know your favorite language")

        return True

    # ---------- TODO LIST ----------

    if command.startswith("add task"):

        task = command.replace("add task", "").strip()

        add_task(task)

        speak("Task added successfully.")

        return True


    elif "show my tasks" in command:

        tasks = show_tasks()

        if not tasks:

            speak("You have no tasks.")

        else:

            speak(f"You have {len(tasks)} tasks.")

            for i, task in enumerate(tasks, start=1):

                print(i, task)

                speak(task)

        return True


    elif "clear all tasks" in command:

        clear_tasks()

        speak("All tasks cleared.")

        return True

    # ---------- REMINDERS ----------

    if command.startswith("remind me to"):

        reminder = command.replace("remind me to", "").strip()

        add_reminder(reminder)

        speak("Reminder added successfully.")

        return True


    elif "show reminders" in command:

        reminders = show_reminders()

        if not reminders:

            speak("You don't have any reminders.")

        else:

            speak(f"You have {len(reminders)} reminders.")

            for i, reminder in enumerate(reminders, start=1):

                print(f"{i}. {reminder}")

                speak(reminder)

        return True


    elif "clear reminders" in command:

        clear_reminders()

        speak("All reminders cleared.")

        return True

    # ---------- ALARM ----------
# ---------- SMART ALARM ----------

    if "set alarm for" in command:

        raw_time = command.split("set alarm for", 1)[1].strip()

        alarm_time = parse_alarm_time(raw_time)

        if alarm_time:

            add_alarm(alarm_time)

            speak(f"Alarm set for {raw_time}")

        else:

            speak("Sorry, I couldn't understand the alarm time.")

        return True

    # ---------- SYSTEM INFO ----------

    if "cpu usage" in command:

        speak(f"CPU usage is {cpu_usage()} percent.")

        return True


    elif "ram usage" in command:

        speak(f"RAM usage is {ram_usage()} percent.")

        return True


    elif "battery percentage" in command or "battery" in command:

        b = battery()

        if b is None:
            speak("Battery information is not available.")
        else:
            speak(f"Battery is at {b} percent.")

        return True


    elif "disk usage" in command:

        speak(f"Disk usage is {disk_usage()} percent.")

        return True

    # ---------------- CLIPBOARD ----------------

    elif "read clipboard" in command:

        text = get_clipboard()

        if text:

            speak("Clipboard contains.")

            speak(text[:300])

        else:

            speak("Clipboard is empty.")

        return True
    
    # ---------------- SCREEN VISION ----------------

    elif (
        "describe my screen" in command
        or "describe screen" in command
        or "what is on my screen" in command
        or "analyze my screen" in command
    ):

        speak("Analyzing your screen. Please wait.")

        result = describe_screen()

        print("\nJarvis:", result)

        speak(result[:300])

        return True

    # ---------------- CAMERA ----------------

    elif (
        "open camera" in command
        or "camera open" in command
        or "start camera" in command
    ):

        speak("Opening camera.")

        result = open_camera()

        print(result)

        speak(result)

        return True

    # ---------------- TAKE PHOTO ----------------

    elif (
        "take photo" in command
        or "take a photo" in command
        or "capture photo" in command
        or "click photo" in command
    ):

        speak("Get ready. Capturing photo in three seconds.")

        result = take_photo()

        print(result)

        speak(result)

        return True

# ---------------- PDF SUMMARY ----------------

    elif (
        "summarize pdf" in command
        or "read pdf" in command
        or "summarize my pdf" in command
        or "open pdf" in command
    ):

        speak("Please select a PDF file.")

        pdf = choose_pdf()

        if not pdf:
            speak("No PDF selected.")
            return True

        speak("Reading your PDF. Please wait.")

        summary = summarize_pdf(pdf)

        print("\nJarvis:", summary)

        speak(summary[:400])

        return True

        # ---------------- OCR ----------------

    elif (
        "read image" in command
        or "read this image" in command
        or "extract text" in command
        or "scan image" in command
    ):

        speak("Please select an image.")

        text = read_image_text()

        print("\nExtracted Text:\n")
        print(text)

        speak(text[:400])

        return True

    # ---------------- FILE SEARCH ----------------

    elif command.startswith("find "):

        filename = command.replace("find", "").strip()

        speak(f"Searching for {filename}")

        results = find_file(filename, r"D:\JARVIS-AI-ASSISTANT")

        if len(results) == 0:
            speak("No matching file found.")
            return True

        print("\nFound Files:\n")

        for file in results:
            print(file)

        speak(f"I found {len(results)} matching file.")
        speak("Opening the first result.")

        os.startfile(results[0])

        return True

    # ---------------- INTERNET SPEED ----------------

    elif (
        "internet speed" in command
        or "check internet speed" in command
        or "speed test" in command
        or "check speed" in command
    ):

        speak("Checking your internet speed. Please wait.")

        result = check_speed()

        print("\n" + result)

        speak(result)

        return True

    # ---------------- VOICE NOTES ----------------

    elif (
        "take a voice note" in command
        or "record voice note" in command
        or "record voice" in command
    ):

        speak("Recording will start now.")

        record_voice(duration=10)

        speak("Voice note saved successfully.")

        return True


    elif (
        "play voice note" in command
        or "play my voice note" in command
    ):

        speak("Playing your voice note.")

        if not play_voice():
            speak("No voice note found.")

        return True
    
    # ---------------- GEMINI AI ----------------
    else:

        speak("Thinking...")

        answer = ask_ai(command)

        if "401" in answer or "UNAUTHENTICATED" in answer:

            speak("Gemini API key is invalid.")

            return True

        print("\nJarvis:", answer)

        speak(answer[:200])

        return True