import pyautogui
import time
import random

def slight_mouse_nudge():
    while True:
        # Get current mouse position
        x, y = pyautogui.position()

        # Move slightly by 1 pixel in a random direction
        dx = random.choice([-1, 1])
        dy = random.choice([-1, 1])
        pyautogui.moveTo(x + dx, y + dy, duration=0.1)

        # Move back to original position
        pyautogui.moveTo(x, y, duration=0.1)

        # Wait 10 seconds before next nudge
        time.sleep(10)

if __name__ == "__main__":
    print("Nudging mouse every 10 seconds.")
    slight_mouse_nudge()
