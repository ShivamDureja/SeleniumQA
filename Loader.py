from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from env import *

# it loads the web page and return the driver
def Loader(url):

    options = Options()
    options._binary_location = chromePath
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(chrome_options=options, executable_path=chromeDriver)
    driver.implicitly_wait(20)
    driver.get(url)
    return driver
