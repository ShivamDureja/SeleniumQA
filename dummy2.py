from distutils.command.sdist import sdist
from bs4 import BeautifulSoup, Tag
import requests


q1 = "Given three equal resistors, how many different combinations (taken all of them together) can be made?"
html_text = requests.get('https://tzflz53oiau.typeform.com/to/BhxbjWXQ').text
soup = BeautifulSoup(html_text,'html.parser')
# fSets = soup.find_all('span',class_ = 'TextWrapper-sc-__sc-1f8vz90-0 dhewSI')
print(soup.prettify())
# for c in fSets:
#     print(c)
ques1 = soup.find(text = f'{q1}')
# for c in ques1:
#     print(ques1)
# print(ques1)




