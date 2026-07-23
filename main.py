import asyncio
import edge_tts
import datetime

VOICE = "en-US-GuyNeural"

async def speak(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("voice.mp3")

    import os
    os.system("start voice.mp3")

async def main():
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    await speak("Hello Nishant! I am Jarvis.")
    await asyncio.sleep(3)

    await speak(f"The time is {current_time}")

asyncio.run(main())