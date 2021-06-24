import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요:')
url = baseUrl + urllib.parse.quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

img = soup.find("div", attrs={"class":"photo_bx api_ani_send _photoBox"})

print(img)

