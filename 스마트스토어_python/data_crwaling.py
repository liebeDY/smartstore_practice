from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip
import pyautogui




class Crawling():
    def __init__(self):
        self.now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        
    
    def chrome_driver(self, url):
        self.url = url
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument("window-size=1920x1080")
        self.browser = webdriver.Chrome("./chromedriver.exe", options=self.options)
        self.browser.get(self.url)
        # print('브라우저를 열고 작업을 실행합니다')
        # print('현재 url : ', self.url)

    def searchlist_maker(self): # 검색할 단어 input으로 받기
        self.searchword_list = []
        self.word = input('검색할 단어를 입력하세요 : ')
        while self.word != " " :
            self.searchword_list.append(self.word)
            self.word = input('검색할 단어를 입력하세요 : ')
        print('검색한 단어 리스트 : ', self.searchword_list)
        return self.searchword_list


    def closeDriver(self):
        self.browser.quit()
        print('브라우저를 종료합니다.')


class Naver(Crawling): # 네이버에서 하는 크롤링 기초 설정
    def __init__(self):
        Crawling.__init__(self)
        self.naver_main_url = "https://www.naver.com/"
        self.naver_search_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
        self.naver_weather_start_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="
        self.naver_weather_end_url = "+%EB%82%A0%EC%94%A8" #? '날씨' 변환


    def weather_url_maker(self, cityname):
        self.cityname = cityname
        self.weather_url = self.naver_weather_start_url+self.cityname+self.naver_weather_end_url
        return self.weather_url

    def search_url_maker(self, searchword):
        self.searchword = searchword
        self.search_url = self.naver_search_url+self.searchword
        return self.search_url

class Naver_weather(Naver):
    def __init__(self):
        Naver.__init__(self)

    def today_weather(self):
        self.stadt_name = self.browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div/span/em').text
        self.temp_today = self.browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/p/span[1]').text+"℃"
        self.kleineinfo = self.browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[1]/p').text
        self.temp_min = self.browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[2]/span[1]/span[1]/span').text+"℃"
        self.temp_max = self.browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[2]/span[1]/span[3]/span').text+"℃"
        self.temp_sensible = self.browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[2]/span[3]').text
        self.rain_fall =  self.browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[3]/span').text
        # print("stadt_name : "+self.stadt_name)
        # print("temp_today : "+self.temp_today)
        # print("kleineinfo : "+self.kleineinfo)
        # print("temp_min : "+self.temp_min)
        # print("temp_max : "+self.temp_max)
        # print("temp_sensible : "+self.temp_sensible)
        # print("rain_fall : "+self.rain_fall)
        # print()
        return self.stadt_name, self.temp_today, self.kleineinfo, self.temp_min, self.temp_max, self.temp_sensible, self.rain_fall


    def time_weather(self):
        for idx in range(1, 9):
            # '날씨' 클릭
            self.browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/a[1]').click()
            self.uhrzeit = self.browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/ul/li[{str(idx)}]/dl/dd[3]/span').text
            self.uhrzeit_temp = self.browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/ul/li[{str(idx)}]/dl/dd[1]/span[1]').text+"℃ "
            self.uhrzeit_condition = self.browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/ul/li[{str(idx)}]/dl/dd[2]/span').text
            
            if len(self.uhrzeit_condition) == 1:   
                self.uhrzeit_condition = self.uhrzeit_condition+"      "
            elif len(self.uhrzeit_condition) == 2: 
                self.uhrzeit_condition = self.uhrzeit_condition+"    "
            elif len(self.uhrzeit_condition) == 3:  
                self.uhrzeit_condition = self.uhrzeit_condition+"  "
            
            # '강수' 클릭
            self.browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/a[2]').click()
            self.uhrzeit_rainfall = self.browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[3]/ul/li[{str(idx)}]/dl/dd[1]').text
            self.uhrzeit_rainrate = self.browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[3]/ul/li[{str(idx)}]/dl/dd[2]/span').text
            
            if len(self.uhrzeit_rainfall) == 3:
                self.uhrzeit_rainfall = self.uhrzeit_rainfall+" "
            if len(self.uhrzeit_rainfall) == 2:
                self.uhrzeit_rainfall = self.uhrzeit_rainfall+"  "
            if len(self.uhrzeit_rainfall) == 1:
                self.uhrzeit_rainfall = self.uhrzeit_rainfall+"   "

            # '습도' 클릭
            self.browser.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/a[4]').click()
            self.uhrzeit_humidity = self.browser.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[5]/ul/li[{str(idx)}]/dl/dd[1]').text
            
            self.uhrzeit_info = f"{self.uhrzeit} {self.uhrzeit_temp} {self.uhrzeit_condition} 습도: {self.uhrzeit_humidity} 강수확률: {self.uhrzeit_rainfall} 예상 강수량: {self.uhrzeit_rainrate}"
            print(self.uhrzeit_info)
        print()


