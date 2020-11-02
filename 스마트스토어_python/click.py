import pyautogui
from time import sleep
import keyboard

print(pyautogui.position())
print(pyautogui.size())



while True:
    pyautogui.click(1285, 427)
    # btn = pyautogui.locateOnScreen("C:/Users/Dong/Desktop/캡쳐/2020-10-13 002.png")
    # print(btn)
    print(pyautogui.position())
    print(pyautogui.size())
    sleep(1)


    pyautogui.press('Enter')
    sleep(1)
    if keyboard.is_pressed('F4'): # F3 누르면
        # print("F3을 눌렀습니다.")
        break # while문 탈출







