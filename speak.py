import asyncio
import edge_tts
import pygame
import os

VOICE = "en-US-GuyNeural"

async def _speak(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("voice.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()

    try:
        os.remove("voice.mp3")
    except:
        pass

def speak(text):
    print("Jarvis:", text)
    asyncio.run(_speak(text))