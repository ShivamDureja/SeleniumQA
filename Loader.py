from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# it loads the web page and return the driver
def Loader(url):

    options = Options()
    options._binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(
        chrome_options=options,
        executable_path="D:\SeleniumChromedriver\chromedriver.exe",
    )
    driver.implicitly_wait(20)
    driver.get(url)
    return driver
