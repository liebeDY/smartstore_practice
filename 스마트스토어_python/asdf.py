import requests
from bs4 import BeautifulSoup
import csv

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
url = 'https://datalab.naver.com/keyword/realtimeList.naver?age=all&datetime=2020-08-15T13%3A13%3A00'
res = requests.get(url,headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
ranks = soup.find("ol", attrs={"id":"realTimeRankFavorite"}).find_all("li")
print(soup)
f = open("네이버 웹툰 인기 순외.csv", 'w', encoding='utf-8-sig', newline="")
wirter = csv.writer(f)
wirter.writerow(['제목','링크'])

for idx, rank in enumerate(ranks):
    text = rank.a.get_text(),"https://comic.naver.com"+rank.a["href"]
    print(str(idx+1)+" 위 :",rank.a.get_text(),"https://comic.naver.com"+rank.a["href"])
    print()
    wirter.writerow(text)
    
