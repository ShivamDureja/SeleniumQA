import time
import random

# function to mimic human typing 
def slow_type(pageElem, pageInput):
    for letter in pageInput:
        time.sleep(float(random.uniform(0.05, 0.3)))
        pageElem.send_keys(letter)
