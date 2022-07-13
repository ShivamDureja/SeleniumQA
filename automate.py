from selenium.webdriver.common.by import By
import time

def automate(driver,dataList):
    questionList = getQuestionDivsFromWeb(driver)
    first = "Given three equal resistors, how many different combinations (taken all of them together) can be made?"
    for questionDiv in questionList:
        print("LOADING QUESTION")
        questions = questionDiv.find_elements(by=By.TAG_NAME, value="span")
        # selectOption(questionDiv, "3")
        for q in questions:
            if(q.text == first):
                print(q.tag_name)
        # questionSpan = questions[3]
        # print(questions.tag_name)
        # questionElement = question.find_element(by=By.TAG_NAME, value="span")
        # questionText = questionElement.text
        # print(questionText)
        # found = 0
        # questionData = []
        # for list in dataList:
        #     print("Working for question : " + questionText)
        #     if list[0] == questionText:
        #         found = 1
        #         questionData = list
        # if found:
        #     selectOption(questionElement, questionData[5])
        #     time.sleep(1)
        
def traverse(path,ques):
    for i in range(ques):
        time.sleep(1)
        path.click()

def getQuestionDivsFromWeb(driver):
    fSets = driver.find_elements(by=By.TAG_NAME, value="fieldset")
    # for sets in fSets:
    #     print(sets.tag_name)
    return fSets


def selectOption(parent, answer):
    print("MOVING TO SELECT OPTION")
    # pXpath = parent.find_element(by=By.XPATH, value="../../../../..")
    # print("pXpath : " + pXpath.tag_name)
    wrapper = parent.find_element(by=By.CLASS_NAME, value="fZIlJA")
    # print(wrapper.tag_name)
    option = wrapper.find_element(by=By.XPATH, value= f"//div[@aria-label='{answer}']")
    time.sleep(5)
    option.click()
    time.sleep(5)

