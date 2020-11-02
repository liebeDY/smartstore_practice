import os
import pyautogui
import pyperclip
import pandas as pd
import selenium
import requests
from bs4 import BeautifulSoup
import urllib.parse
from selenium import webdriver
# 사업 관련된 클래스 
# 1. 폴더 만들기 
# 1-1 경로 설정
# 1-2 경로에 폴더 확인, 없으면 생성 / 있으면 경로 반환
# 1-3 csv 파일로 저장


# 2. 셀레니움 / 웹드라이버 설정
# 2-1 웹드라이버 불러오기 mit 옵션
# 2-2 셀레니움 불러오기 mit Url


# 3. Pyautogui 설정
# 3-1 카카오톡 자동 보내기 

# 4. Pandas 설정
# 4-1 csv 파일 불러오기 : 1-3 파일
# 4-2 취합해서 분석 툴 만들기

class MeinArbeit():
    def __init__(self):
        self.mainpath = "C:/Users/Dong/Desktop/사업/"

    def folderMaker(self, path) : # 폴더 생성 : 인자값 - 원하는 폴더 명 / 폴도 생성 후 폴더 명 return
        self.arbeitPath = self.mainpath+path
        print(f"현재 경로 : {self.arbeitPath}")

        if not os.path.exists(self.arbeitPath):
            os.mkdir(self.arbeitPath)
            print(f'{self.arbeitPath} 폴더를 생성하였습니다.')
            return self.arbeitPath
        else :
            return self.arbeitPath
        

    def csvMaker(self, filename, mode, *contents): # 사업 폴더에 csv 파일로 저장 후 파일 이름을 return
        '''
            filename : 파일 이름
            mode : "w" 쓰기, "a" 이어서 쓰기, "r" 읽기
            contents : 내용, 리스트로 받는다 
        '''
        self.filename = filename
        self.mode = mode
        self.contents = list(contents)

        with open(f"{self.arbeitPath}/{self.filename}.csv", self.mode, encoding="utf-8-sig") as self.f:
            for self.content in self.contents :
                self.f.write(self.content+"\n")
        return self.filename


class KakaoArbeit(MeinArbeit) : # 카카오로 작업 할 것
    def __init__(self):             # MeinArbeit class 상속
        MeinArbeit.__init__(self) 
        self.capturePath = "C:/Users/Dong/Desktop/캡쳐/"

    def profileSelect(self, filename): #! 듀얼모니터에서 확인 해보세요!!!!!
        self.profilePath = self.capturePath+filename
        print(self.profilePath)
        self.profileSelect_btn = pyautogui.locateOnScreen(f"{self.profilePath}")
        self.center = pyautogui.center(self.profileSelect_btn)
        print(self.center)
        pyautogui.doubleClick(self.center)
        
    def toProfile_msg(self, *contents): # profileSelect 이후에 실행할 것
        self.msg_content_list = list(contents)
        for self.idx, self.msg_content in enumerate(self.msg_content_list):
            pyperclip.copy(f"{self.idx} : {self.msg_content}\n")
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.keyDown('shift')  
            pyautogui.press('enter')            
            pyautogui.keyUp('shift')  
        pyautogui.press('enter') # 메세지 보내기
            

class PandasArbeit(MeinArbeit) : # Pandas 작업 할 것
    def __init__(self):             # MeinArbeit class 상속
        MeinArbeit.__init__(self) 
        self.pandasPath = "C:/Users/Dong/Desktop/사업/"

    def fileLoad(self, filename):  # Pandas로 파일 전체 불러오기
        self.pandasFilename = self.pandasPath+filename
        pass

    def analyse(self): # Pandas 로 분석 하기
        pass

    def graph(self): # Pandas 분석한것 그래프로 그리기
        pass

    def fileSave(self): # 파일 저장하기 : xlms
        pass







class Crwaling(MeinArbeit) : # 크롤링 할 때 
    def __init__(self):             # MeinArbeit class 상속
        MeinArbeit.__init__(self) 
        self.driverPath = "./chromedriver.exe"

    

    def change_searchWord(self, originalword): # quote_plus 로 단어 변환하기 
        self.originalword = originalword
        self.changedword = urllib.parse.quote_plus(self.originalword)
        print('입력한 단어 : '+self.originalword)
        print('변환된 단어 : '+self.changedword)
        return self.changedword




class RequestsArbeit(Crwaling) : # Requests 로 작업 할 것
    def __init__(self):             # MeinArbeit class 상속
        Crwaling.__init__(self) 



