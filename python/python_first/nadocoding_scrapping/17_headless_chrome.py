from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

import time
interval = 2

# 현재 문서 높이 저장
prev_heigth = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)

    current_height = browser.execute_script("return document.body.scrollHeight")
    
    if current_height == prev_heigth:
        break
    
    prev_heigth = current_height
    
print("스크롤 완료")



import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)
