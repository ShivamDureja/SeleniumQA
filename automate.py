from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from slowTyping import slow_type

quesCount = 9
currentIndex = 0

# main automate function
def automate(driver, dataList):
    global quesCount
    time.sleep(2)
    i = 0
    NotFoundQues = ""
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
            # select the correct option 
            selectOption(selectedFSet, ans, val, currQ[6])
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
    fSets = driver.find_elements(by=By.XPATH, value="//*[@data-qa='question-wrapper']")
    return fSets

# to select the correct option according to its type
def selectOption(fieldset, answer, val, qType):
    if qType == "mcq":
        option = fieldset.find_element(
            by=By.XPATH, value=f".//div[@aria-label='{answer}']"
        )
        option.click()
        time.sleep(2)
    elif qType == "fib":
        option = fieldset.find_element(by=By.TAG_NAME, value="textarea")
        option.click()
        slow_type(option, val)
        time.sleep(2)
        clickOk = fieldset.find_element(by=By.TAG_NAME, value="button")
        clickOk.click()
    elif qType == "linked":
        option = fieldset.find_element(by=By.TAG_NAME, value="input")
        option.click()
        slow_type(option, val)
        time.sleep(2)
        clickOk = fieldset.find_element(by=By.TAG_NAME, value="button")
        clickOk.click()
