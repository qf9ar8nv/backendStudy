import requests

Url = "http://google.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
res = requests.get(Url, headers=headers)

with open("tistory.html", "w", encoding="utf8") as f:
    f.write(res.text)