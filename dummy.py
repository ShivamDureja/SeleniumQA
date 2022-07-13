from Loader import Loader
from selenium.webdriver.common.by import By
import time
from fetchData import fetchList
# from find import clickElement

page_url = "https://tzflz53oiau.typeform.com/to/BhxbjWXQ"
local_path = "D:\\SMDEVOPS\\SeleniumQA\\QnA.xlsx"
driver = Loader(page_url)
dataList = fetchList(local_path)
time.sleep(2)

ques = "The speed at which tjie current travels in a conductor is nearly:"
ans = "3 × 104 ms-1"
# my_element = driver.find_element_by_xpath("//span[text()='" + text +"']").text
text1 = driver.find_elements(by=By.XPATH, value=f"//span[text()='{ques}']/parent::node()/parent::node()/parent::node()/parent::node()/parent::node()/child::div[@class='SpacerWrapper-sc-__sc-4rs8xl-0 eWJrrP']/child::node()/child::div[@role='radiogroup']/child::node()/child::node()/child::div[@aria-label='{ans}']")
#//div[@class='SpacerWrapper-sc-__sc-4rs8xl-0 eWJrrP']//div[contains(text(),'{ans}')]")
# print(text1[3].tag_name)
for c in text1:
    print(c.text)


time.sleep(2)
driver.close()


# CurrQuest2 = driver.find_element(by=method, value="/html[1]/body[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[2]/span[1]/span[1]").text
# time.sleep(2)
# print(CurrQuest2)
# okButton = driver.find_element(by=method, value= "/html[1]/body[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
# okButton.click()
# time.sleep(2)
# CurrQuest3 = driver.find_element(by=method, value="/html[1]/body[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[2]/span[1]/span[1]").text
# time.sleep(2)
# print(CurrQuest3)
# okButton = driver.find_element(by=method, value= "/html[1]/body[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
# okButton.click()
# time.sleep(2)
# CurrQuest4 = driver.find_element(by=method, value="/html[1]/body[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[2]/span[1]/span[1]").text
# time.sleep(2)
# print(CurrQuest4)
# okButton = driver.find_element(by=method, value= "/html[1]/body[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
# okButton.click()
# time.sleep(2)
# CurrQuest5 = driver.find_element(by=method, value="/html[1]/body[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[2]/span[1]/span[1]").text
# time.sleep(2)
# print(CurrQuest5)
# okButton = driver.find_element(by=method, value= "/html[1]/body[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
# okButton.click()
# time.sleep(2)
# CurrQuest6 = driver.find_element(by=method, value="/html[1]/body[1]/div[3]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[2]/span[1]/span[1]").text
# time.sleep(2)
# print(CurrQuest6)

