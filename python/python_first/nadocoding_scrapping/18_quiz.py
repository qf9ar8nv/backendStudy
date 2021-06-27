from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://new.land.naver.com/")

browser.find_element_by_id("search_input").send_keys("대전 엑슬루 타워")
browser.find_element_by_class_name("button_search--icon").click()

try:
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "item_inner ")))
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    items = soup.find_all("a", attrs={"class":"item_link"})
    
    for idx, item in enumerate(items):
        title = item.find("span", attrs={"class":"type"}).get_text()
        price = item.find("span", attrs={"class":"price"}).get_text()
        spec = item.find("span", attrs={"class":"spec"}).get_text().split(", ")
        position = item.find("span", attrs={"class":"text"}).get_text()
        area = spec[0]
        height = spec[1]
        print("*" * 20 + " 매물{} ".format(idx+1) + "*" * 20)
        print("거래 : " + title)
        print("면적 : " + area)
        print("가격 : " + price)
        print("동 : " + position)
        print("층 : " + height)

except:
    browser.quit()
