import time
import random
import pyautogui
from env import *

# function to mimic human typing
def slow_type(pageElem, pageInput):
    for letter in pageInput:
        time.sleep(float(random.uniform(0.05, 0.3)))
        pageElem.send_keys(letter)


# function to mimic human mouse movement
def mouseMovement(location, size, panelHeight, panelWidth):
    xPos = location["x"]
    yPos = location["y"]
    sizeX = size["width"]
    sizeY = size["height"]
    xFinal = xPos + sizeX / 2
    yFinal = yPos + sizeY / 2

    pyautogui.moveTo(
        x=xFinal,
        y=yFinal + panelHeight + additionalHeight,
        duration=mouseTime,
        tween=pyautogui.easeInOutQuad,
    )
