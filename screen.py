import pyautogui

def capture_screen(filename="screen.png"):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return filename