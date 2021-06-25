import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://www.google.com/search?q=%EC%82%AC%EA%B3%BC&sxsrf=ALeKk03BqEA7aHRUtvEA6hE14DpJIdLTNg:1624619249906&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiQmqSq0rLxAhWSNKYKHco2CUQQ_AUoAXoECAEQAw&biw=958&bih=959"
browser.get(url)

soup = BeautifulSoup(browser.page_source, "lxml")

imgs = soup.find_all("div", attrs={"class":"isv-r PNCib MSM1fd BUooTd"})
print(len(imgs))

for idx, image in enumerate(imgs):
    print(idx)
    image = imgs[idx].find("img", attrs={"class":"rg_i Q4LuWd"})
    name = image.get('src')
    if name == None:
        continue
    if name.startswith("http"):
        image_res = requests.get(name)
        image_res.raise_for_status()

        with open("apple{}.jpg".format(idx+1), "wb") as h:
            h.write(image_res.content)
    else:
        with urlopen(name) as f:
            with open("apple{}.jpg".format(idx+1), "wb") as h:
                img_src = f.read()
                h.write(img_src)

    

browser.quit()