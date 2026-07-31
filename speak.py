import asyncio
import edge_tts
import pygame
import os
from langdetect import detect

pygame.mixer.init()


def get_voice(text):
    try:
        lang = detect(text)

        if lang == "hi":
            return "hi-IN-MadhurNeural"      # Hindi Male

        return "en-US-GuyNeural"             # English Male

    except:
        return "en-US-GuyNeural"


async def _tts(text):

    voice = get_voice(text)

    filename = "voice.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice
    )

    await communicate.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()

    if os.path.exists(filename):
        os.remove(filename)


def speak(text):
    try:
        asyncio.run(_tts(text))
    except Exception:
        print(f"Jarvis: {text}")