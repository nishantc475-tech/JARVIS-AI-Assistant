import customtkinter as ctk
import threading
import subprocess
import sys

from ai import ask_ai
from speak import speak
from listen import listen
from sidebar import Sidebar

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("JARVIS AI Assistant")
app.geometry("1200x750")


# =======================
# Functions
# =======================

def send_message():

    question = entry.get().strip()

    if question == "":
        return

    chat_box.insert("end", f"\n\nYou: {question}\n")
    chat_box.see("end")

    entry.delete(0, "end")

    def run_ai():

        answer = ask_ai(question)

        speak(answer)

        app.after(
            0,
            lambda: (
                chat_box.insert("end", f"\nJarvis: {answer}\n"),
                chat_box.see("end")
            )
        )

    threading.Thread(target=run_ai, daemon=True).start()


def voice_chat():

    chat_box.insert("end", "\n🎤 Listening...\n")
    chat_box.see("end")

    question = listen()

    if not question:
        chat_box.insert("end", "\nJarvis: I couldn't hear you.\n")
        return

    chat_box.insert("end", f"\nYou: {question}\n")
    chat_box.see("end")

    def run_ai():

        answer = ask_ai(question)

        speak(answer)

        app.after(
            0,
            lambda: (
                chat_box.insert("end", f"\nJarvis: {answer}\n"),
                chat_box.see("end")
            )
        )

    threading.Thread(target=run_ai, daemon=True).start()


def open_camera():
    try:
        subprocess.Popen([sys.executable, "camera.py"])
    except Exception as e:
        chat_box.insert("end", f"\nCamera Error: {e}\n")


def image_mode():
    chat_box.insert("end", "\n🖼 Image feature coming soon...\n")


def pdf_mode():
    chat_box.insert("end", "\n📄 PDF feature coming soon...\n")


def weather_mode():
    chat_box.insert("end", "\n🌦 Weather feature coming soon...\n")


def news_mode():
    chat_box.insert("end", "\n📰 News feature coming soon...\n")


def settings_mode():
    chat_box.insert("end", "\n⚙ Settings feature coming soon...\n")


# =======================
# Sidebar
# =======================

sidebar = Sidebar(
    app,
    {
        "voice": lambda: threading.Thread(target=voice_chat, daemon=True).start(),
        "camera": open_camera,
        "image": image_mode,
        "pdf": pdf_mode,
        "weather": weather_mode,
        "news": news_mode,
        "settings": settings_mode,
    }
)

sidebar.pack(side="left", fill="y")


# =======================
# Main Frame
# =======================

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
title.pack(pady=20)


status = ctk.CTkLabel(
    main_frame,
    text="🟢 Status : Online",
    font=("Arial", 18)
)
status.pack(pady=5)


chat_box = ctk.CTkTextbox(
    main_frame,
    width=900,
    height=420,
    font=("Consolas", 16)
)

chat_box.pack(pady=20)

chat_box.insert("end", "Jarvis is ready...\n")


entry = ctk.CTkEntry(
    main_frame,
    width=750,
    placeholder_text="Type your message..."
)

entry.pack(pady=10)

entry.bind("<Return>", lambda event: send_message())


send_btn = ctk.CTkButton(
    main_frame,
    text="Send",
    width=180,
    command=send_message
)

send_btn.pack(pady=8)


voice_btn = ctk.CTkButton(
    main_frame,
    text="🎤 Talk to Jarvis",
    width=220,
    height=40,
    command=lambda: threading.Thread(
        target=voice_chat,
        daemon=True
    ).start()
)

voice_btn.pack(pady=5)


app.mainloop()