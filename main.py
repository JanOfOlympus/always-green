import pyautogui
import time
import random
import keyboard

def move_mouse_randomly(interval_seconds):
    try:
        while True:
            # Get the screen size
            screen_width, screen_height = pyautogui.size()

            # Generate random x and y coordinates within the screen boundaries
            x = random.randint(0, screen_width - 1)
            y = random.randint(0, screen_height - 1)

            # Move the mouse to the new coordinates
            pyautogui.moveTo(x, y, duration=0.5)

            # Wait for the specified interval
            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("Mouse movement stopped.")

if __name__ == "__main__":
    # Set the interval in seconds
    interval_seconds = 5
    move_mouse_randomly(interval_seconds)