from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("path-to-chromedriver")
driver.get("https://www.netify.ai/resources/applications")
time.sleep(31)
content = driver.page_source

soup = BeautifulSoup(content)
tbody_element = soup.find('tbody')
trows = tbody_element.find_all('tr')
category = ""
for trow in trows:
  child = trow.findChild('h3')
  if child is not None:
    category = child.string
  else:
    img = trow.findChild('img', alt= True)
    appName = img['alt'].split('-')[0]
    netifyUrl = trow.findChild('td', {"class": "hidden-xs"}).string
    print(appName.rstrip() + ',' + category.rstrip() + ',' + netifyUrl.rstrip() )
