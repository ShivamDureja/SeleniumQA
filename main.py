from Loader import Loader
from fetchData import fetchList
from automate import automate
from env import *

page_url = pageUrl
local_path = qFile_path
driver = Loader(page_url)
my_list = fetchList(local_path)
driver.maximize_window()
panelHeight = driver.execute_script("return window.outerHeight - window.innerHeight;")
panelWidth = driver.execute_script("return window.innerWidth;")
automate(driver, my_list, panelHeight, panelWidth)
