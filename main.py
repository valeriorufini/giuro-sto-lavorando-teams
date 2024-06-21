import pyautogui
import time
import math

# Configura i parametri del movimento circolare
center_x, center_y = pyautogui.size().width / 2, pyautogui.size().height / 2
radius = 100
num_steps = 100
delay = 0.01  # Secondi di ritardo tra ogni movimento

# Muovi il mouse in un cerchio continuo
while True:
    for step in range(num_steps):
        angle = 2 * math.pi * step / num_steps
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        pyautogui.moveTo(x, y)
        time.sleep(delay)
