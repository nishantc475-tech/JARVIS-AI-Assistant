import os
import subprocess
import shutil
import webbrowser
from speak import speak


def handle_apps(command):

    # ---------- CODING MODE ----------
    if "coding mode" in command or "start coding" in command:

        speak("Starting coding mode.")

        try:
            subprocess.Popen("code", shell=True)
        except:
            speak("VS Code is not installed.")

        webbrowser.open("https://github.com")
        webbrowser.open("https://chatgpt.com")

        return True
    # ---------- DEVELOPER MODE ----------
    if "developer mode" in command:

        speak("Developer mode activated.")

        try:
            subprocess.Popen("code", shell=True)
        except:
            speak("VS Code is not installed.")

        subprocess.Popen("start cmd", shell=True)

        webbrowser.open("https://github.com")
        webbrowser.open("https://chatgpt.com")

        return True
    
    # ---------- STUDY MODE ----------
    if "study mode" in command:

        speak("Study mode activated.")

        webbrowser.open("https://chatgpt.com")

        try:
            subprocess.Popen("notepad", shell=True)
        except:
            pass

        return True

    # Calculator
    if "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")
        return True

    # Notepad
    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
        return True

    # VS Code
    elif "open vscode" in command:
        speak("Opening Visual Studio Code")
        os.system("code")
        return True

    # Desktop
    elif "open desktop" in command:

        speak("Opening Desktop")

        try:
            os.system("explorer.exe shell:desktop")
        except Exception:
            speak("Unable to open Desktop")

        return True

    # Downloads
    elif "open downloads" in command:

        speak("Opening Downloads")

        downloads = os.path.join(os.path.expanduser("~"), "Downloads")

        os.startfile(downloads)

        return True

    # Documents
    elif "open documents" in command:

        speak("Opening Documents")

        try:
            os.system("explorer.exe shell:personal")
        except Exception:
            speak("Unable to open Documents")

        return True

    # D Drive
    elif command == "open d drive" or command == "open d":

        speak("Opening D Drive")

        os.startfile("D:\\")

        return True

    # Generic App Opening
    elif command.startswith("open "):

        app = command.replace("open ", "").strip()

        websites = {
            "google",
            "youtube",
            "github",
            "gmail",
            "chatgpt",
            "instagram",
            "facebook",
            "amazon",
            "flipkart",
            "linkedin",
            "spotify",
        }

        if app in websites:
            return False

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
            speak(f"Opening {app}")
            subprocess.Popen(apps[app], shell=True)
            return True

        exe = shutil.which(app)

        if exe:
            speak(f"Opening {app}")
            subprocess.Popen(exe)
            return True

    return False