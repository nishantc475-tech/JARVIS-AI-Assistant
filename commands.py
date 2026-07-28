from speak import speak
from ai import ask_ai
from memory import remember, recall
import webbrowser
import os
import requests
import mss
import subprocess
import psutil
import shutil
from weather import get_weather
from news import get_news
from datetime import datetime


def execute(command):

    command = command.lower()

    # ---------------- GOOGLE ----------------
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # ---------------- YOUTUBE ----------------
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # ---------------- CALCULATOR ----------------
    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    # ---------------- NOTEPAD ----------------
    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    # ---------------- TIME ----------------
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # ---------------- VS CODE ----------------
    elif "open vscode" in command:
        speak("Opening Visual Studio Code")
        os.system("code")

    # ---------------- WHATSAPP ----------------
    elif "open whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    # ---------------- SPOTIFY ----------------
    elif "open spotify" in command:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")

    # ---------------- GITHUB ----------------
    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    # ---------------- LINKEDIN ----------------
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    # ---------------- INSTAGRAM ----------------
    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    # ---------------- GMAIL ----------------
    elif "open gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    # ---------------- CHATGPT ----------------
    elif "open chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    # ---------------- MEMORY ----------------
    elif "remember my name is" in command:

        name = command.replace("remember my name is", "").strip()

        remember("name", name)

        speak(f"Okay, I will remember your name is {name}")

    elif "what is my name" in command:

        name = recall("name")

        if name:
            speak(f"Your name is {name}")
        else:
            speak("I don't know your name yet")

    elif "remember my favorite language is" in command:

        language = command.replace(
            "remember my favorite language is", "").strip()

        remember("language", language)

        speak(f"I will remember your favorite language is {language}")

    elif "what is my favorite language" in command:

        language = recall("language")

        if language:
            speak(f"Your favorite language is {language}")
        else:
            speak("I don't know your favorite language")

                # ---------------- GOOGLE SEARCH ----------------
    elif "search google for" in command:

        query = command.replace("search google for", "").strip()

        speak(f"Searching Google for {query}")

        webbrowser.open(
            f"https://www.google.com/search?q={query.replace(' ', '+')}"
        )

    # ---------------- YOUTUBE SEARCH ----------------
    elif "search youtube for" in command:

        query = command.replace("search youtube for", "").strip()

        speak(f"Searching YouTube for {query}")

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        )

    # ---------------- FACEBOOK ----------------
    elif "open facebook" in command:

        speak("Opening Facebook")

        webbrowser.open("https://www.facebook.com")

    # ---------------- AMAZON ----------------
    elif "open amazon" in command:

        speak("Opening Amazon")

        webbrowser.open("https://www.amazon.in")

    # ---------------- FLIPKART ----------------
    elif "open flipkart" in command:

        speak("Opening Flipkart")

        webbrowser.open("https://www.flipkart.com")

            # ---------------- SCREENSHOT ----------------
    # ---------------- SCREENSHOT ----------------
    elif "take screenshot" in command or "take a screenshot" in command:

      try:
        with mss.mss() as sct:
            filename = sct.shot(output="screenshot.png")

        speak("Screenshot saved successfully.")
        print("Saved:", filename)

      except Exception as e:
        print(e)
        speak("Sorry, I could not take the screenshot.")

    # ---------------- OPEN DOWNLOADS ----------------
    elif "open downloads" in command:

        speak("Opening Downloads folder")

        downloads = os.path.join(os.path.expanduser("~"), "Downloads")

        os.startfile(downloads)

    # ---------------- OPEN DESKTOP ----------------
    elif "open desktop" in command:

       speak("Opening Desktop")

       try:
           os.system("explorer.exe shell:desktop")
       except Exception:
           speak("Unable to open Desktop")


    # ---------------- OPEN DOCUMENTS ----------------
    elif "open documents" in command:

       speak("Opening Documents")

       try:
           os.system("explorer.exe shell:personal")
       except:
           speak("Unable to open Documents")
 
    # ---------------- OPEN D DRIVE ----------------
    elif command == "open d drive" or command == "open d":

        speak("Opening D Drive")

        os.startfile("D:\\")

      # ---------------- PLAY MUSIC ----------------
    elif "play music" in command:

      folders = [
         os.path.join(os.environ["USERPROFILE"], "Music"),
         "D:\\Music",
         "D:\\Songs",
         "D:\\Downloads"
      ]

      found = False

      for folder in folders:

          if os.path.exists(folder):

               for file in os.listdir(folder):

                  if file.endswith((".mp3", ".wav")):

                     speak("Playing music")
                     os.startfile(os.path.join(folder, file))
                     found = True
                     break

          if found:
                  break

      if not found:
            speak("No music file found.")



                 # ---------------- WEATHER ----------------
    elif "weather" in command:
            
          city = "Dehradun"
            
          if "in " in command:
                    city = command.split("in ", 1)[1].strip()
            
                    result = get_weather(city)
            
                    print(result)
            
                    speak(result)
            
                        
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

      # ----------------OPEN ANY WEBSITE----------------
    elif command.startswith("open "):

         app = command.replace("open ", "").strip()

      # Website commands ko skip karo
         websites = [
         "google", "youtube", "github", "gmail",
         "chatgpt", "instagram", "facebook",
         "amazon", "flipkart", "linkedin", "spotify"
      ]

         if app not in websites:

           exe = shutil.which(app)

           if exe:
               speak(f"Opening {app}")
               subprocess.Popen(exe)
               return

         # Common Windows apps
           apps = {
               "paint": "mspaint",
               "calculator": "calc",
               "notepad": "notepad",
               "cmd": "cmd",
               "explorer": "explorer",
               "word": "winword",
               "excel": "excel",
               "powerpoint": "powerpnt",
         }

           if app in apps:
               try:
                  speak(f"Opening {app}")
                  subprocess.Popen("start cmd", shell=True)
                  return
               except Exception:
                  pass

         speak(f"I couldn't find {app}.")

    # ---------------- BATTERY ----------------
    elif "battery" in command:

        battery = psutil.sensors_battery()

        if battery:

            percent = battery.percent

            if battery.power_plugged:
                status = "charging"
            else:
                status = "not charging"

            message = f"Battery is {percent} percent and {status}."

            print(message)

            speak(message)

        else:

            speak("Battery information is not available.")    

            # ---------------- CPU ----------------
    elif "cpu" in command:

        cpu = psutil.cpu_percent(interval=1)

        message = f"CPU usage is {cpu} percent."

        print(message)

        speak(message)


# ---------------- RAM ----------------
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

        # ---------------- DATE ----------------
    elif "date" in command:

        today = datetime.now().strftime("%d %B %Y")

        message = f"Today's date is {today}."

        print(message)

        speak(message)


# ---------------- DAY ----------------
    elif "day" in command:

        current_day = datetime.now().strftime("%A")

        message = f"Today is {current_day}."

        print(message)

        speak(message)

# ---------------- DISK STORAGE ----------------
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

        # ---------------- PUBLIC IP ----------------
    elif "ip address" in command or "my ip" in command:

       try:

            ip = requests.get("https://api.ipify.org").text

            message = f"Your public IP address is {ip}"

            print(message)

            speak(message)

       except Exception:

            speak("Sorry, I could not get your IP address.")

         # ---------------- AI ----------------
    else:

            speak("Thinking...")

            answer = ask_ai(command)

            if "401" in answer or "UNAUTHENTICATED" in answer:
                speak("Gemini API key is invalid.")
                return

            print("\nJarvis:", answer)
            speak(answer[:200])