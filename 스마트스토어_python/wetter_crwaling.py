
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from Geschaefts_Module import Crwaling
from pymongo import MongoClient 
from pymongo.cursor import CursorType

host = "localhost" 
port = "27017" 
mongo = MongoClient(host, int(port)) 
db = mongo['weather_database']
weather_collection = db['weather']

print("db : ", db)
print()
print("weather_collection : ", weather_collection)


now = time.strftime('%Y-%m-%d', time.localtime(time.time()))



a = Crwaling()
ort = "안양"
ort_2 = a.change_searchWord(ort)
# print(ort_2)
search_url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={ort_2}+%EB%82%A0%EC%94%A8'

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
browser = webdriver.Chrome(a.driverPath, options=options)
browser.get(search_url)
print('브라우저를 열고 작업을 실행 합니다.\n')
print("search_url : "+search_url+"\n")


stadt_name = browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div/span/em').text
temp_today = browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/p/span[1]').text+"℃"


kleineinfo = browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[1]/p').text
temp_min = browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[2]/span[1]/span[1]/span').text+"℃"
temp_max = browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[2]/span[1]/span[3]/span').text+"℃"
temp_sensible = browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[2]/span[3]').text
rain_fall =  browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[3]/span').text

weather_collection.insert_one({
    "현재 시간" : now,
    "도시" : stadt_name,
    "현재 온도" : temp_today,
    "현재 날씨" : kleineinfo,
    "최저 온도" : temp_min,
    "최고 온도" : temp_max,
    "체감 온도" : temp_sensible,
    "강수량" : rain_fall
})
print("weather_collection 에 저장하였습니다.")
print()

print("stadt_name : "+stadt_name)
print("temp_today : "+temp_today)
print("kleineinfo : "+kleineinfo)
print("temp_min : "+temp_min)
print("temp_max : "+temp_max)
print("temp_sensible : "+temp_sensible)
print("rain_fall : "+rain_fall)
print()
print("시간대별 날씨\n")

# for idx in range(1, 9):
#     browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/a[1]').click()
#     uhrzeit = browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/ul/li[{str(idx)}]/dl/dd[3]/span').text
#     uhrzeit_temp = browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/ul/li[{str(idx)}]/dl/dd[1]/span[1]').text+"℃ "
#     uhrzeit_condition = browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/ul/li[{str(idx)}]/dl/dd[2]/span').text
    
#     if len(uhrzeit_condition) == 1:
#         uhrzeit_condition = uhrzeit_condition+"  "
    

#     browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/a[2]').click()
#     uhrzeit_rainfall = browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[3]/ul/li[{str(idx)}]/dl/dd[1]').text
#     uhrzeit_rainrate = browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[3]/ul/li[{str(idx)}]/dl/dd[2]/span').text
    
#     browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/a[4]').click()
#     uhrzeit_humidity = browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[5]/ul/li[{str(idx)}]/dl/dd[1]').text
    
#     uhrzeit_info = f"{uhrzeit} {uhrzeit_temp} {uhrzeit_condition} 습도: {uhrzeit_humidity} 강수 확률: {uhrzeit_rainfall} 예상 강수량: {uhrzeit_rainrate}"
#     print(uhrzeit_info)

browser.quit()


for result in weather_collection.find():
    print("result : ", result)
    # weather_collection.delete_many({})
    
print(weather_collection.find())
print()
print('완료되었습니다.')