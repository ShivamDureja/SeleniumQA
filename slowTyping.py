import time
import random


def slow_type(pageElem, pageInput):
    for letter in pageInput:
        time.sleep(float(random.uniform(.05, .3)))
        pageElem.send_keys(letter)  