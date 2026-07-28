import os
import mss
from speak import speak


def handle_media(command):

    # ---------------- SCREENSHOT ----------------
    if "take screenshot" in command or "take a screenshot" in command:

        try:

            with mss.mss() as sct:
                filename = sct.shot(output="screenshot.png")

            speak("Screenshot saved successfully.")
            print("Saved:", filename)

        except Exception as e:

            print(e)
            speak("Sorry, I could not take the screenshot.")

        return True

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

        return True

    return False