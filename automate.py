from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
# from htmlToPdf import convert_html_to_pdf
# from xhtml2pdf import pisa 

quesCount = 9
currentIndex = 0

def automate(driver,dataList):
    global quesCount
    time.sleep(2)
    i = 0
    NotFoundQues = ""
    for i in range (quesCount):
        fSets = getQuestionDivsFromWeb(driver)
        if(i == 0):
            fset = fSets[0]
        elif(i==quesCount-1):
            fset = fSets[len(fSets)-1]
        else:
            fset = fSets[1]
        ques = None
        selectedFSet = None
        currQ = None
        soup = BeautifulSoup(fset.get_attribute('innerHTML'),"html.parser")
        i = i + 1
        for list in dataList:
            # print("Matching with : " + list[0])
            ques = soup.find(text = f'{list[0]}')
            if(ques != None):
                currQ = list
                selectedFSet = fset
                # print(f"Working ON QUESTION: {ques}")
                break
        if(selectedFSet != None):
            ans = soup.find(text = f'{currQ[5]}')
            val = currQ[1]
            selectOption(selectedFSet,ans,val, currQ[6])
            time.sleep(2)
        else:
            NotFoundQues = NotFoundQues + fset.get_attribute('innerHTML')
            if(i == len(fSets)):
                continue
            traverse(0,1,driver)
    SubmitForm()

def SubmitForm():
    print("Form Submitted")

def findNav(driver, index):
    nav = driver.find_element(by=By.CLASS_NAME, value = "Navigation-sc-__sc-1ckh2u2-4")
    btn = nav.find_elements(by=By.TAG_NAME, value = "button")
    if(index != -1):
        return btn[index]
    return btn

def maintainIndex(direction):
    global currentIndex
    if direction:
        currentIndex = currentIndex + 1
    else:
        currentIndex = currentIndex - 1

def traverse(index,clicks, driver):
    global currentIndex
    if(index == 0):
        if(clicks+currentIndex > quesCount):
            return
    if(index == 1):
        if(currentIndex-clicks < 0):
            return
    for i in range(clicks):
        time.sleep(1)
        try:
            btn = findNav(driver, index)
            btn.click()
            if(index == 0):
                maintainIndex(1)
            else:
                maintainIndex(0)
        except:
            btn = findNav(driver, index)
            btn.click()
            if(index == 0):
                maintainIndex(1)
            else:
                maintainIndex(0)

# returns all fieldsets from page in form a list
def getQuestionDivsFromWeb(driver):
    fSets = driver.find_elements(by=By.XPATH, value="//*[@data-qa='question-wrapper']")
    return fSets

def selectOption(fieldset,answer,val,qType):
    if(qType == "mcq"):
        option = fieldset.find_element(by=By.XPATH, value=f".//div[@aria-label='{answer}']")
        option.click()
        time.sleep(2)
    elif(qType == "fib"):
        option = fieldset.find_element(by=By.TAG_NAME, value="textarea")
        option.click()
        option.send_keys(val)
        time.sleep(2)
        clickOk = fieldset.find_element(by=By.TAG_NAME, value="button")
        clickOk.click()
    elif(qType == "linked"):
        option = fieldset.find_element(by=By.TAG_NAME, value="input")
        option.click()
        option.send_keys(val)
        time.sleep(2)
        clickOk = fieldset.find_element(by=By.TAG_NAME, value="button")
        clickOk.click()


    
    
