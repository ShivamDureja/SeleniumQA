import time
import random
import pyautogui
import numpy as np
import bezier

# function to mimic human typing
def slow_type(pageElem, pageInput):
    for letter in pageInput:
        time.sleep(float(random.uniform(0.05, 0.3)))
        pageElem.send_keys(letter)


def mouseMovement(location, size, panelHeight):
    x, relY = location["x"], location["y"]  ##abs X and relative Y
    absY = relY + panelHeight
    w, h = size["width"], size["height"]
    wCenter = w / 2
    hCenter = h / 2
    xCenter = int(wCenter + x)
    yCenter = int(hCenter + absY)

    start = pyautogui.position()
    end = xCenter, yCenter

    x2 = (start[0] + end[0]) / 2  # midpoint x
    y2 = (start[1] + end[1]) / 2  ##midpoint y

    control1X = (start[0] + x2) / 2
    control1Y = (end[1] + y2) / 2

    control2X = (end[0] + x2) / 2
    control2Y = (start[1] + y2) / 2

    # Two intermediate control points that may be adjusted to modify the curve.
    control1 = control1X, y2  ##combine midpoints to create perfect curve
    control2 = control2X, y2

    # Format points to use with bezier
    control_points = np.array([start, control1, control2, end])
    points = np.array(
        [control_points[:, 0], control_points[:, 1]]
    )  # Split x and y coordinates

    # You can set the degree of the curve here, should be less than # of control points
    degree = 3

    # Create the bezier curve
    curve = bezier.Curve(points, degree)

    curve_steps = 50  # How many points the curve should be split into. Each is a separate pyautogui.moveTo() execution
    delay = 0.003  # Time between movements. 1/curve_steps = 1 second for entire curve

    # Move the mouse
    for j in range(1, curve_steps + 1):
        # The evaluate method takes a float from [0.0, 1.0] and returns the coordinates at that point in the curve
        # Another way of thinking about it is that i/steps gets the coordinates at (100*i/steps) percent into the curve
        x, y = curve.evaluate(j / curve_steps)
        pyautogui.moveTo(x, y)  # Move to point in curve
        pyautogui.sleep(delay)  # Wait delay
