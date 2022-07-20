from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from humanMimicking import slow_type
from humanMimicking import mouseMovement
import pyautogui
import time
from env import *

quesCount = QuesCount
currentIndex = 0

# main automate function
def automate(driver, dataList, panelH, panelWidth):
    global quesCount
    time.sleep(2)
    i = 0
    # traverse to each and every question
    for i in range(quesCount):
        # list to store all the wrapper elements of every question
        fSets = getQuestionDivsFromWeb(driver)
        if i == 0:
            fset = fSets[0]
        elif i == quesCount - 1:
            fset = fSets[len(fSets) - 1]
        else:
            fset = fSets[1]
        ques = None
        selectedFSet = None
        currQ = None
        soup = BeautifulSoup(fset.get_attribute("innerHTML"), "html.parser")
        i = i + 1
        for list in dataList:
            # find the question from screen
            ques = soup.find(text=f"{list[0]}")
            if ques != None:
                # update list and current fset accordingly
                currQ = list
                selectedFSet = fset
                break
        if selectedFSet != None:
            # find the ans to the corresponding question value
            ans = soup.find(text=f"{currQ[5]}")
            val = currQ[1]
            # to select the correct option
            selectOption(selectedFSet, ans, val, currQ[6], panelH, panelWidth)
            time.sleep(2)
        else:
            if i == len(fSets):
                continue
            traverse(0, 1, driver)
    SubmitForm()


def SubmitForm():
    print("Form Submitted")


# to find the parent element of buttons
def findNav(driver, index):
    nav = driver.find_element(by=By.CLASS_NAME, value="Navigation-sc-__sc-1ckh2u2-4")
    btn = nav.find_elements(by=By.TAG_NAME, value="button")
    if index != -1:
        return btn[index]
    return btn


def maintainIndex(direction):
    global currentIndex
    if direction:
        currentIndex = currentIndex + 1
    else:
        currentIndex = currentIndex - 1


# to traverse the form if question is not present
def traverse(index, clicks, driver):
    global currentIndex
    if index == 0:
        if clicks + currentIndex > quesCount:
            return
    if index == 1:
        if currentIndex - clicks < 0:
            return
    for i in range(clicks):
        time.sleep(1)
        try:
            btn = findNav(driver, index)
            btn.click()
            if index == 0:
                maintainIndex(1)
            else:
                maintainIndex(0)
        except:
            btn = findNav(driver, index)
            btn.click()
            if index == 0:
                maintainIndex(1)
            else:
                maintainIndex(0)


# returns all wrapper elements from page in form a list
def getQuestionDivsFromWeb(driver):
    fSets = driver.find_elements(by=By.XPATH, value=WrapperValue)
    return fSets


# to select the correct option according to its type
def selectOption(fieldset, answer, val, qType, panelH, panelWidth):
    if qType == "mcq":
        option = fieldset.find_element(
            by=By.XPATH, value=f".//div[@aria-label='{answer}']"
        )
        locate = option.location
        size = option.size
        mouseMovement(locate, size, panelH, panelWidth)
        option.click()
    elif qType == "fib":
        option = fieldset.find_element(by=By.TAG_NAME, value=FibValue)
        option.click()
        locate = option.location
        size = option.size
        mouseMovement(locate, size, panelH, panelWidth)
        slow_type(option, val)
        time.sleep(2)
        pressOk(fieldset)
    elif qType == "linked":
        option = fieldset.find_element(by=By.TAG_NAME, value=LinkedValue)
        locate = option.location
        length = option.size
        mouseMovement(locate, length, panelH, panelWidth)
        slow_type(option, val)
        pressOk(fieldset)


def pressOk(parent):
    clickOk = parent.find_element(by=By.TAG_NAME, value="button")
    clickOk.click()
