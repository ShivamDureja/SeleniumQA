from Loader import Loader
from fetchData import fetchList
from automate import automate

page_url = "https://tzflz53oiau.typeform.com/to/BhxbjWXQ"
local_path = "D:\\SMDEVOPS\\SeleniumQA\\Book 1.xlsx"
driver = Loader(page_url)
my_list = fetchList(local_path)
# print(my_list)
automate(driver,my_list)






