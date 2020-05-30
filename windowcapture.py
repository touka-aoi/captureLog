#https://teratail.com/questions/147319
#https://ocome85.work/2019/11/04/37/#toc11 神
#https://pyautogui.readthedocs.io/en/latest/keyboard.html
#http://blog.livedoor.jp/pythonsuezo/archives/8791049.html
#https://stackoverrun.com/ja/q/12912920
#https://note.nkmk.me/python-pillow-basic/
#https://www.programcreek.com/python/example/89840/win32gui.ShowWindow


#参考 https://ocome85.work/2019/11/04/37/
#アクティブウィンドウ名
#アクティブウィンドいち
#アクティブウィンドウサイズ
#キャプチャーでおk


#一つ前のアクティブウィンドウIDからウィンドサイズと位置を取得してキャプチャーしていいかんじにかこうてぎたらなー

import tkinter
import pyautogui
import win32gui
import win32con
import threading
import time
import sys
import queue
import datetime
from PIL import Image, ImageGrab
import re


global dataQ

#アクティブウィンドウの取得
def getForeWindow():
    while True:
        a = win32gui.GetForegroundWindow()
        print(a)
        dataQ.put(a)
        time.sleep(3)
        # 終了措置
        if len(threading.enumerate()) == 2:
            print("are?")
            sys.exit()

#一秒前のアクティブウィンドゲット
def getBeoreForeWindo():
    a = dataQ.get()
    return a


#画像をとる
#アクティブ化して、alt+priおす、クリップボードからとってくる。
#
#
#
def captureScreen():
    nowTime = datetime.datetime.now()
    myTkWin = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(myTkWin, win32con.SW_HIDE)
    time.sleep(1)
    beforeActive = getBeoreForeWindo()
    beforeActiveTitle = win32gui.GetWindowText(beforeActive)
    te = re.split(" ", beforeActiveTitle)
    firstShepe = te[0]
    secondShape = te[len(te) - 1]
    print(firstShepe + "-" + secondShape + nowTime.strftime(" %m-%d-%Y %H-%M-%S"))
    win32gui.SetForegroundWindow(beforeActive)
    pyautogui.hotkey("alt", "printscreen")
    sc = ImageGrab.grabclipboard()
    # ドットがあるとバグる
    sc.save("./store/" + firstShepe + "-" + secondShape + nowTime.strftime(" %m-%d-%Y %H-%M-%S") + ".png")
    win32gui.ShowWindow(myTkWin, win32con.SW_SHOW)



# 終了措置
def stopingpower():
    sys.exit()

#GUI操作
def createWindowPop():
    root = tkinter.Tk()
    root.title("rara")
    root.geometry("100x150")
    # 10倍される？
    button = tkinter.Button(text="実行ボタン", height=10, width=15, command=captureScreen)
    button.place(x=0, y=0)
    quit_botton = tkinter.Button(text="おわり！", height=10, width=15, command=stopingpower)
    quit_botton.place(x=0, y=180)
    root.attributes("-topmost", True)
    root.mainloop()

#スレッド違うから好きにいじれない


dataQ = queue.LifoQueue()

thread2 = threading.Thread(target=createWindowPop)
thread1 = threading.Thread(target=getForeWindow)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
