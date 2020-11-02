from data_crwaling import Naver_weather
from data_crwaling import Naver
from data_crwaling import Crawling
import time
from mongodb_wetter import WetterMongodb

now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

a = Naver_weather()
weather_collection = WetterMongodb()

citylist = ['서울','인천','대전','부산','대구','광주']

print("현재 시간 : ", now)

wetter_list = []
for ort in citylist :
    search_url = a.weather_url_maker(ort)
    
    a.chrome_driver(search_url)

    city, temp, info, temp_min, temp_max, temp_sensible, rain_fall = a.today_weather()
    info = info.split(",")[0]
    temp_sensible = temp_sensible.split("체감온도 ")[1]

    print(city)
    print(temp)
    print(info)
    print(temp_min)
    print(temp_max)
    print(temp_sensible)
    print(rain_fall)
    
    a.time_weather()
    
    wetter_template = weather_collection.wetterlistsave(city,info,temp,temp_min,temp_max)
    wetter_list.append(wetter_template)

# print("wetter_list : ", wetter_list)


weather_collection.datasave(now, wetter_list)

a.closeDriver()

# print(weather_collection.alldatafind())
