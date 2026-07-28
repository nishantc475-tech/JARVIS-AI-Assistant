from speak import speak
from ai import ask_ai
from memory import remember, recall
from modules.apps import handle_apps
from modules.web import handle_web
from modules.system import handle_system
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

    if handle_system(command):
        return
    
    if handle_apps(command):
        return
    
    if handle_web(command):
        return


    # ---------------- TIME ----------------
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")



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



         # ---------------- AI ----------------
    else:

            speak("Thinking...")

            answer = ask_ai(command)

            if "401" in answer or "UNAUTHENTICATED" in answer:
                speak("Gemini API key is invalid.")
                return

            print("\nJarvis:", answer)
            speak(answer[:200])