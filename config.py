import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
# ================= AI =================

AI_MODELS = [
    "gemini-flash-latest",
    "gemini-3.6-flash",
    "gemini-2.0-flash",
    "gemini-2.5-flash"
]

# ================= PROJECT =================

PROJECT_NAME = "Jarvis AI Assistant"
VERSION = "2.0"
AUTHOR = "Nishant Chauhan"

# ================= VOICES =================

DEFAULT_VOICE = "en-US-GuyNeural"
HINDI_VOICE = "hi-IN-MadhurNeural"

# ================= PATHS =================

PROJECT_FOLDER = r"D:\JARVIS-AI-ASSISTANT"

DOWNLOADS = os.path.join(os.environ["USERPROFILE"], "Downloads")
DESKTOP = os.path.join(os.environ["USERPROFILE"], "Desktop")
DOCUMENTS = os.path.join(os.environ["USERPROFILE"], "Documents")
PICTURES = os.path.join(os.environ["USERPROFILE"], "Pictures")

# ================= FILES =================

MEMORY_FILE = "memory.json"
TODO_FILE = "tasks.json"
REMINDER_FILE = "reminders.json"
ALARM_FILE = "alarms.json"