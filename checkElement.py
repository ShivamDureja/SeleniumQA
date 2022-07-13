from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element(by=By.XPATH, value = xpath)
        print("ELEMENT FOUND")
    except NoSuchElementException:
        print("NOT FOUND")
        return False
    return True