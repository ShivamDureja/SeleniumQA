from Loader import Loader
from fetchData import fetchList
from automate import automate

page_url = "https://tzflz53oiau.typeform.com/to/BhxbjWXQ"
local_path = "D:\\SMDEVOPS\\SeleniumQA\\removedQ.xlsx"
driver = Loader(page_url)
my_list = fetchList(local_path)
automate(driver,my_list)
driver.close()


