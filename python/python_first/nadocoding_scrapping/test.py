import requests
res = requests.get("http://google.com")

print("응답코드 :", res.status_code)

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)