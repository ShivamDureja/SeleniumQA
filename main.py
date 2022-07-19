from Loader import Loader
from fetchData import fetchList
from automate import automate

page_url = "https://tzflz53oiau.typeform.com/to/n7eaeDxl"
local_path = "D:\\SMDEVOPS\\SeleniumQA\\updatedQues.xlsx"
driver = Loader(page_url)
my_list = fetchList(local_path)
panelHeight = driver.execute_script('return window.outerHeight - window.innerHeight;')
# print(my_list)
driver.maximize_window()
automate(driver, my_list,panelHeight)
