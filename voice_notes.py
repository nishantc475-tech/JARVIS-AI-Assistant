import os
import sounddevice as sd
from scipy.io.wavfile import write
import winsound

VOICE_FOLDER = "voice_notes"

os.makedirs(VOICE_FOLDER, exist_ok=True)


def record_voice(filename="note.wav", duration=10):

    filepath = os.path.join(VOICE_FOLDER, filename)

    fs = 44100

    print("Recording...")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filepath, fs, recording)

    return filepath


def play_voice(filename="note.wav"):

    filepath = os.path.join(VOICE_FOLDER, filename)

    if not os.path.exists(filepath):
        return False

    winsound.PlaySound(filepath, winsound.SND_FILENAME)

    return True