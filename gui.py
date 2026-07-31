import customtkinter as ctk
import threading

from ai import ask_ai
from speak import speak
from listen import listen
from image_picker import choose_image
from vision import describe_image
from camera import take_photo
from pdf_reader import choose_pdf, summarize_pdf
from weather import get_weather
from news import get_news
from history import save_chat, clear_history, load_history

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

    settings.title("⚙ Settings")
    settings.geometry("400x350")

    settings.grab_set()

    title = ctk.CTkLabel(
        settings,
        text="JARVIS Settings",
        font=("Arial", 22, "bold")
    )
    title.pack(pady=20)

    appearance = ctk.CTkLabel(
        settings,
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


buttons = [
    ("🏠 Home", None),
    ("💬 Chat", None),
    ("🎤 Voice", lambda: threading.Thread(target=voice_chat, daemon=True).start()),
    ("📷 Camera", camera_mode),
    ("🖼 Image", image_mode),
    ("📄 PDF", pdf_mode),
    ("🌦 Weather", weather_mode),
    ("📰 News", news_mode),
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

app.mainloop()