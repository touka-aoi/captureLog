#マウス位置取得

import pyautogui
import time

while True:
    a = pyautogui.position()
    print(a)
    time.sleep(1)

    #Point(x=-1022, y=-387)