import subprocess
import webbrowser

def open_app(app_name):

    app = app_name.lower()

    apps = {
        "notepad": "notepad",
        "calculator": "calc",
        "paint": "mspaint",
        "cmd": "cmd",
        "explorer": "explorer",
        "task manager": "taskmgr",
        "control panel": "control"
    }

    if app in apps:
        subprocess.Popen(apps[app])
        return f"Opening {app_name}."

    return "Application not found."

def open_website(site):

    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "chatgpt": "https://chat.openai.com",
        "gmail": "https://mail.google.com",
        "linkedin": "https://www.linkedin.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com"
    }

    site = site.lower()

    if site in websites:
        webbrowser.open(websites[site])
        return f"Opening {site}."

    return "Website not found."