import customtkinter as ctk
import threading

from ai import ask_ai
from speak import speak
from listen import listen
from image_picker import choose_image
from vision import describe_image, describe_screen
from camera import take_photo
from pdf_reader import choose_pdf, summarize_pdf
from weather import get_weather
from news import get_news
from history import save_chat, clear_history, load_history
from web_search import search_web
from memory import remember, recall, clear_memory
from memory import remember, recall, recall_all, forget


# -----------------------------
# Theme
# -----------------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# -----------------------------
# Main Window
# -----------------------------
app = ctk.CTk()
app.title("🤖 JARVIS AI Assistant")
app.geometry("1200x750")
app.minsize(1000, 650)

# -----------------------------
# Sidebar
# -----------------------------
sidebar = ctk.CTkFrame(
    app,
    width=220,
    corner_radius=0
)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

title_sidebar = ctk.CTkLabel(
    sidebar,
    text="🤖 JARVIS",
    font=("Arial", 26, "bold")
)
title_sidebar.pack(pady=(25, 20))


def send_message():

    question = entry.get().strip()

    question_lower = question.lower()

    # Show everything Jarvis remembers
    if (
        "what do you remember about me" in question_lower
        or "what do you know about me" in question_lower
    ):

        data = recall_all()

        if not data:

            answer = "I don't remember anything about you yet."

        else:

            answer = "Here's what I remember about you:\n\n"

            for key, value in data.items():
                answer += f"{key.title()} : {value}\n"

        chat_box.insert("end", f"\nJarvis: {answer}\n")
        chat_box.see("end")

        speak("Here is what I remember about you.")

        return

    # Forget memory

    if question_lower.startswith("forget "):

        key = question[7:].strip().lower()

        if forget(key):

            answer = f"I forgot your {key}."

        else:

            answer = f"I don't remember any {key}."

        chat_box.insert("end", f"\nJarvis: {answer}\n")
        chat_box.see("end")

        speak(answer)

        return

    # My name is ...
    if question_lower.startswith("my name is "):
        value = question[11:].strip()
        remember("name", value)

        answer = f"Nice to meet you, {value}."

        chat_box.insert("end", f"\nJarvis: {answer}\n")
        chat_box.see("end")

        speak(answer)
        return


    # I live in ...
    if question_lower.startswith("i live in "):
        value = question[10:].strip()
        remember("city", value)

        answer = f"I'll remember that you live in {value}."

        chat_box.insert("end", f"\nJarvis: {answer}\n")
        chat_box.see("end")

        speak(answer)
        return


    # My favourite ...
    if question_lower.startswith("my favourite "):

        try:
            data = question[13:]

            key, value = data.split(" is ", 1)

            key = "favourite " + key.strip().lower()
            value = value.strip()

            remember(key, value)

            answer = f"I'll remember your favourite {key.replace('favourite ', '')} is {value}."

            chat_box.insert("end", f"\nJarvis: {answer}\n")
            chat_box.see("end")

            speak(answer)
            return

        except:
            pass

    # Remember anything
    if question_lower.startswith("remember "):

        try:
            data = question[9:]

            key, value = data.split(" is ", 1)

            key = key.strip().lower()
            value = value.strip()

            remember(key, value)

            answer = f"I'll remember your {key} is {value}."

            chat_box.insert("end", f"\nJarvis: {answer}\n")
            chat_box.see("end")

            speak(answer)

            return

        except:

            answer = "Use: Remember hobby is coding"

            chat_box.insert("end", f"\nJarvis: {answer}\n")
            speak(answer)

            return


    # Recall memory
    if question_lower.startswith("what is my "):

        key = question_lower.replace("what is my ", "").strip()

        value = recall(key)

        if value:

            answer = f"Your {key} is {value}."

        else:

            answer = f"I don't know your {key} yet."

        chat_box.insert("end", f"\nJarvis: {answer}\n")
        chat_box.see("end")

        speak(answer)

        return

    if question == "":
        return

    chat_box.insert("end", f"\nYou: {question}\n")
    chat_box.see("end")

    entry.delete(0, "end")

    set_status("🟡 Thinking...")

    def run_ai():

        answer = ask_ai(question)
        save_chat("Jarvis", answer)

        speak(answer)

        app.after(
            0,
            lambda: (
                chat_box.insert("end", f"\nJarvis: {answer}\n"),
                chat_box.see("end"),
            )
        )

        set_status("🟢 Status : Online")

    threading.Thread(target=run_ai, daemon=True).start()


def voice_chat():

    set_status("🎤 Listening...")

    question = listen()

    if not question:

        set_status("🟢 Status : Online")
        chat_box.insert("end", "\nJarvis: I couldn't hear you.\n")
        chat_box.see("end")

        return

    chat_box.insert("end", f"\nYou: {question}\n")
    save_chat("You", question)
    chat_box.see("end")

    def run_ai():

        answer = ask_ai(question)
        save_chat("Jarvis", answer)

        speak(answer)

        app.after(
            0,
            lambda: (
                chat_box.insert("end", f"\nJarvis: {answer}\n"),
                chat_box.see("end"),
            )
        )

        set_status("🟢 Status : Online")

    threading.Thread(target=run_ai, daemon=True).start()


def image_mode():

    image_path = choose_image()

    if not image_path:
        return

    chat_box.insert("end", "\n🖼 Image selected.\n")
    chat_box.insert("end", "🤖 Analyzing image...\n")
    chat_box.see("end")

    set_status("🟣 Vision AI...")

    def run_ai():

        answer = describe_image(image_path)
        save_chat("Jarvis", answer)

        speak(answer)

        app.after(
            0,
            lambda: (
                chat_box.insert("end", f"\nJarvis: {answer}\n"),
                chat_box.see("end"),
            )
        )

        set_status("🟢 Status : Online")

    threading.Thread(target=run_ai, daemon=True).start()

def screen_mode():

    chat_box.insert("end", "\n🖥 Capturing screen...\n")
    chat_box.see("end")

    set_status("🖥 Screen Analysis...")

    def run_ai():

        answer = describe_screen()

        speak(answer)

        save_chat("Jarvis", answer)

        app.after(
            0,
            lambda: (
                chat_box.insert("end", f"\nJarvis: {answer}\n"),
                chat_box.see("end")
            )
        )

        set_status("🟢 Status : Online")

    threading.Thread(
        target=run_ai,
        daemon=True
    ).start() 

def camera_mode():

    set_status("📷 Opening Camera...")

    image_path = take_photo()

    if not image_path:
        set_status("🟢 Status : Online")
        return

    chat_box.insert("end", "\n📷 Photo captured.\n")
    chat_box.insert("end", "🤖 Analyzing image...\n")
    chat_box.see("end")

    set_status("🟣 Vision AI...")

    def run_ai():

        answer = describe_image(image_path)
        save_chat("Jarvis", answer)

        speak(answer)

        app.after(
            0,
            lambda: (
                chat_box.insert("end", f"\nJarvis: {answer}\n"),
                chat_box.see("end"),
                set_status("🟢 Status : Online")
            )
        )

    threading.Thread(target=run_ai, daemon=True).start()


def pdf_mode():

    pdf_path = choose_pdf()

    if not pdf_path:
        return

    chat_box.insert("end", "\n📄 PDF selected.\n")
    chat_box.insert("end", "🤖 Reading PDF...\n")
    chat_box.see("end")

    set_status("📄 Reading PDF...")

    def run_ai():

        answer = summarize_pdf(pdf_path)
        save_chat("Jarvis", answer)

        speak(answer)

        app.after(
            0,
            lambda: (
                chat_box.insert("end", f"\nJarvis: {answer}\n"),
                chat_box.see("end")
            )
        )

        set_status("🟢 Status : Online")

    threading.Thread(target=run_ai, daemon=True).start()


def weather_mode():

    city = entry.get().strip()

    if city == "":
        city = "Dehradun"

    chat_box.insert("end", f"\n🌦 Checking weather for {city}...\n")
    chat_box.see("end")

    set_status("🌦 Fetching Weather...")

    def run_ai():

        answer = get_weather(city)
        save_chat("Jarvis", answer)

        speak(answer)

        app.after(
            0,
            lambda: (
                chat_box.insert("end", f"\nJarvis: {answer}\n"),
                chat_box.see("end")
            )
        )

        set_status("🟢 Status : Online")

    threading.Thread(target=run_ai, daemon=True).start()

def search_mode():

    query = entry.get().strip()

    if query == "":
        return

    chat_box.insert("end", f"\n🔍 Searching: {query}\n")
    chat_box.see("end")

    entry.delete(0, "end")

    set_status("🌐 Searching Web...")

    def run_search():

        result = search_web(query)

        save_chat("Jarvis", result)

        app.after(
            0,
            lambda: (
                chat_box.insert("end", f"\nJarvis:\n{result}\n"),
                chat_box.see("end")
            )
        )

        speak("Search completed.")

        set_status("🟢 Status : Online")

    threading.Thread(
        target=run_search,
        daemon=True
    ).start()


def news_mode():

    chat_box.insert("end", "\n📰 Fetching latest news...\n")
    chat_box.see("end")

    set_status("📰 Fetching News...")

    def run_ai():

        answer = get_news()
        save_chat("Jarvis", answer)

        speak(answer)

        app.after(
            0,
            lambda: (
                chat_box.insert("end", f"\nJarvis:\n{answer}\n"),
                chat_box.see("end")
            )
        )

        set_status("🟢 Status : Online")

    threading.Thread(target=run_ai, daemon=True).start()

def clear_chat():

    chat_box.delete("1.0", "end")

    chat_box.insert("end", "Jarvis is ready...\n")

    clear_history()

    set_status("🟢 Status : Online")


def settings_mode():

    settings = ctk.CTkToplevel(app)

    settings_mode.title("⚙ Settings")
    settings_mode.geometry("400x350")

    settings_mode.grab_set()

    title = ctk.CTkLabel(
        settings_mode,
        text="JARVIS Settings",
        font=("Arial", 22, "bold")
    )
    title.pack(pady=20)

    appearance = ctk.CTkLabel(
        settings_mode,
        text="Appearance Mode",
        font=("Arial", 16)
    )
    appearance.pack(pady=10)

    def dark():

        ctk.set_appearance_mode("Dark")

    def light():

        ctk.set_appearance_mode("Light")

    def system():

        ctk.set_appearance_mode("System")

    dark_btn = ctk.CTkButton(
        settings,
        text="🌙 Dark Mode",
        command=dark
    )
    dark_btn.pack(pady=8)

    light_btn = ctk.CTkButton(
        settings,
        text="☀ Light Mode",
        command=light
    )
    light_btn.pack(pady=8)

    system_btn = ctk.CTkButton(
        settings,
        text="💻 System Mode",
        command=system
    )
    system_btn.pack(pady=8)

    about = ctk.CTkLabel(
        settings,
        text="JARVIS AI Assistant\nVersion 1.0\nMade by Nishant",
        font=("Arial", 14)
    )
    about.pack(pady=25)    


buttons = [
    ("🏠 Home", None),
    ("💬 Chat", None),
    ("🎤 Voice", lambda: threading.Thread(target=voice_chat, daemon=True).start()),
    ("📷 Camera", camera_mode),
    ("🖼 Image", image_mode),
    ("🖥 Screen AI", screen_mode),
    ("📄 PDF", pdf_mode),
    ("🌦 Weather", weather_mode),
    ("📰 News", news_mode),
    ("🌐 Web Search", search_mode),
    ("⚙ Settings", settings_mode),
]

for text, cmd in buttons:

    btn = ctk.CTkButton(
        sidebar,
        text=text,
        width=180,
        height=40,
        command=cmd
    )

    btn.pack(pady=6)

version = ctk.CTkLabel(
    sidebar,
    text="JARVIS v1.0\nMade by Nishant",
    font=("Arial", 12)
)
version.pack(side="bottom", pady=20)

# -----------------------------
# Main Area
# -----------------------------
main_frame = ctk.CTkFrame(app)
main_frame.pack(
    side="right",
    fill="both",
    expand=True
)

title = ctk.CTkLabel(
    main_frame,
    text="🤖 JARVIS AI Assistant",
    font=("Arial", 30, "bold")
)
title.pack(pady=(20, 5))

status = ctk.CTkLabel(
    main_frame,
    text="🟢 Status : Online",
    font=("Arial", 18)
)

status.pack()

def set_status(text):
    app.after(
        0,
        lambda: status.configure(text=text)
    )

chat_box = ctk.CTkTextbox(
    main_frame,
    font=("Consolas", 15)
)
chat_box.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)

history = load_history()

if history.strip():

    chat_box.insert(
        "end",
        "\n========== Previous Chat ==========\n\n"
    )

    chat_box.insert("end", history)

    chat_box.insert(
        "end",
        "\n===================================\n\n"
    )

chat_box.insert("end", "Jarvis is ready...\n")

chat_box.see("end")

bottom_frame = ctk.CTkFrame(main_frame)
bottom_frame.pack(
    fill="x",
    padx=20,
    pady=(0, 20)
)

entry = ctk.CTkEntry(
    bottom_frame,
    placeholder_text="Type your message..."
)
entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 10)
)

entry.bind("<Return>", lambda e: send_message())

send_btn = ctk.CTkButton(
    bottom_frame,
    text="Send",
    width=100,
    command=send_message
)
send_btn.pack(side="left", padx=5)

voice_btn = ctk.CTkButton(
    bottom_frame,
    text="🎤",
    width=60,
    command=lambda: threading.Thread(
        target=voice_chat,
        daemon=True
    ).start()
)
voice_btn.pack(side="left")

clear_btn = ctk.CTkButton(
    bottom_frame,
    text="🗑",
    width=60,
    command=clear_chat
)

clear_btn.pack(side="left", padx=5)



app.mainloop()