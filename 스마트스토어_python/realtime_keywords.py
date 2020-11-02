from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip
import pyautogui

# five_btn = pyautogui.locateOnScreen("C:/Users/Dong/Desktop/캡쳐/kakaotalk_myprofil.png")
# center = pyautogui.center(five_btn)
# print(center)
# 실시간 검색어
#날짜 별로 폴더 만들기
#10대, 20대, 30대, 40대, 50대, 전체 별로 파일 만들기

now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
folderdate = time.strftime('%Y-%m-%d',time.localtime(time.time()))

workingpath = f"C:/Users/Dong/Desktop/사업/검색어/{folderdate}/"


def folderMaker(path):
    try :
        if not os.path.exists(path):
            os.mkdir(path)

    except :
        print('오류 입니다.')

# 웹드라이버 설정
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

# 크롬 드라이버 열기 / 네이버 실시간 검색어
browser = webdriver.Chrome("./chromedriver.exe", options=options)
browser.get('https://datalab.naver.com/keyword/realtimeList.naver')
print('브라우저를 열고 작업을 실행 합니다.\n')

# 관심사 설정
browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[1]/div/div/a[5]').click()
browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[2]/div/div/a[5]').click()
browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[3]/div/div/a[5]').click()
browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[4]/div/div/a[5]').click()
browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[5]/div/div/a[5]').click()

# 세대 별로 실시간 검색어 추출 /csv 파일로 각 날짜별 폴더에 저장
for search_idx in range(1, 7):
    browser.find_element_by_xpath(f'//*[@id="content"]/div/div[2]/div[1]/div[2]/div/div/div/ul/li[{search_idx}]').click()
    if search_idx == 6 :
        age = "전체"
    else :
        age = "{}0대".format(str(search_idx))
        
    elem = browser.find_elements_by_class_name('item_title_wrap')

    folderMaker(workingpath)
    screen_file = ".png"
    csv_file = ".csv"
    filename = f"{now} 실시간 {age} 검색어 순위".replace(":",".")
    browser.get_screenshot_as_file(workingpath+filename+screen_file)

    print('--- 현재 실시간 {} 검색어 순위 입니다 ---'.format(age))
    print("--- {}---\n".format(now))
    # pyautogui.doubleClick(center)

    with open(workingpath+filename+csv_file, "a", encoding="utf-8-sig") as f:
        for idx, e in enumerate(elem)  :
            print("{0}위 : {1}".format(str(idx+1), e.text))
            f.write("{0}위 : {1}\n".format(str(idx+1), e.text))
            # pyperclip.copy("{0}위 : {1}\n".format(str(idx+1), e.text))
            
            # pyautogui.hotkey('ctrl', 'v')
            # pyautogui.keyDown('shift')  
            # pyautogui.press('enter')  
    print()
    print('"'+filename+csv_file+'"'+" 파일을 저장하였습니다.")
    print()
    # pyautogui.keyDown('shift')  
    # pyautogui.press('enter') 
    # pyautogui.keyUp('shift')  

print()
print('완료하였습니다')


