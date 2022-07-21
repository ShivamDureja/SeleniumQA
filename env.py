###   VARIABLES   ###

##### for main.py #####
pageUrl = "https://tzflz53oiau.typeform.com/to/n7eaeDxl"
qFile_path = "D:\\SMDEVOPS\\SeleniumQA\\resources\\updatedQues.xlsx"
usersFilePath = "D:\\SMDEVOPS\\SeleniumQA\\resources\\users.xlsx"

##### for automate.py #####
QuesCount = 9
# Value of Xpath of Wrapper element for every question present
WrapperValue = "//*[@data-qa='question-wrapper']"
# value for answer element of type FIB (Tag Name)
FibValue = "textarea"
# value for answer element of type Linked (Tag Name)
LinkedValue = "input"

##### for Loader.py #####
# Enter the location of your chrome.exe
chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# Enter the location of your chrome driver
chromeDriver = "D:\SeleniumChromedriver\chromedriver.exe"

##### for humanMimicking.py #####
# time taken to move mouse (slower the time more is the speed of mouse)
mouseTime = 0.5
# additional vertical height to be added
additionalHeight = 85
