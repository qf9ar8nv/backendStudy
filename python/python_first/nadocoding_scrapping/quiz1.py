import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def create_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def weather_scrapping():
    url_weather = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8"
    soup = create_soup(url_weather)

    wea_1 = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    cur_tem = soup.find("span", attrs={"class":"todaytemp"}).get_text()
    min_tem = soup.find("span", attrs={"class":"min"}).find("span", attrs={"class":"num"}).get_text()
    max_tem = soup.find("span", attrs={"class":"max"}).find("span", attrs={"class":"num"}).get_text()
    mor_rain = soup.find("span", attrs={"class":"point_time morning"}).find("span", attrs={"class":"num"}).get_text()
    aft_rain = soup.find("span", attrs={"class":"point_time afternoon"}).find("span", attrs={"class":"num"}).get_text()

    print("[오늘의 날씨]")
    print(wea_1)
    print("현재 {}℃  (최저 {}℃ / 최고 {}℃)".format(cur_tem,min_tem, max_tem))
    print("오전 강수확률 {}% / 오후 강수확률 {}%".format(mor_rain, aft_rain))
    print("")

    with open("today.txt", "w", encoding="utf8") as f:
        f.write("[오늘의 날씨] \n")
        f.write(wea_1 + "\n")
        f.write("현재 {}℃  (최저 {}℃ / 최고 {}℃) \n".format(cur_tem,min_tem, max_tem))
        f.write("오전 강수확률 {}% / 오후 강수확률 {}% \n".format(mor_rain, aft_rain))
        f.write("\n")

def news_scrapping():
    url_news = "https://news.naver.com"
    soup = create_soup(url_news)

    print("[오늘의 헤드라인]")
    with open("today.txt", "a", encoding="utf8") as f:
            f.write("[오늘의 헤드라인] \n")

    titles = soup.find_all("div", attrs={"class":"hdline_article_tit"})
    links = soup.find_all("div", attrs={"class":"hdline_article_tit"})
    for i in range(3):
        title = titles[i].find("a").get_text().strip()
        link = url_news + links[i].find("a")['href']
        print("{}.".format(i+1), title)
        print("({})".format(link))
        with open("today.txt", "a", encoding="utf8") as f:
            f.write("{}. ".format(i+1) + title + "\n")
            f.write("({}) \n".format(link))


weather_scrapping()
news_scrapping()