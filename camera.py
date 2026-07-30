import cv2
import time
from datetime import datetime


def open_camera():

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        return "Unable to open camera."

    while True:

        ret, frame = camera.read()

        if not ret:
            break

        cv2.imshow("Jarvis Camera", frame)

        key = cv2.waitKey(1)

        # Press Q to quit
        if key == ord("q"):
            break

        # Press S to save photo
        if key == ord("s"):

            filename = datetime.now().strftime(
                "photo_%Y%m%d_%H%M%S.jpg"
            )

            cv2.imwrite(filename, frame)

            camera.release()
            cv2.destroyAllWindows()

            return f"Photo saved as {filename}"

    camera.release()
    cv2.destroyAllWindows()

    return "Camera closed."


def take_photo():

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        return "Unable to open camera."

    print("Capturing photo in 3 seconds...")

    time.sleep(3)

    ret, frame = camera.read()

    if not ret:
        camera.release()
        cv2.destroyAllWindows()
        return "Failed to capture photo."

    filename = datetime.now().strftime(
        "photo_%Y%m%d_%H%M%S.jpg"
    )

    cv2.imwrite(filename, frame)

    camera.release()
    cv2.destroyAllWindows()

    return f"Photo saved as {filename}"