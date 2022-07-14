from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


def automate(driver,dataList):
    time.sleep(2)
    nav = driver.find_element(by=By.CLASS_NAME, value = "Navigation-sc-__sc-1ckh2u2-4")
    btn = nav.find_elements(by=By.TAG_NAME, value = "button")
    fSets = getQuestionDivsFromWeb(driver)
    i = 0
    for fset in fSets:
        ques = None
        selectedFSet = None
        currQ = None
        soup = BeautifulSoup(fset.get_attribute('innerHTML'),"html.parser")
        i = i + 1
        for list in dataList:
            ques = soup.find(text = f'{list[0]}')
            if(ques != None):
                currQ = list
                selectedFSet = fset
        if(selectedFSet != None):
            ans = soup.find(text = f'{currQ[5]}')
            selectOption(selectedFSet,ans)
            time.sleep(2)
        else:
            if(i == len(fSets)):
                continue
            traverse(btn[0],1)


def traverse(path,clicks):
    for i in range(clicks):
        time.sleep(1)
        path.click()

def getQuestionDivsFromWeb(driver):
    fSets = driver.find_elements(by=By.TAG_NAME, value="fieldset")
    return fSets

def selectOption(fieldset,answer):
    option = fieldset.find_element(by=By.XPATH, value=f".//div[@aria-label='{answer}']")
    option.click()
    time.sleep(2)
