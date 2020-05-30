#https://teratail.com/questions/147319
#https://ocome85.work/2019/11/04/37/#toc11 神


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

global root
global dataQ

#アクティブウィンドウの取得
def getForeWindow():
    while True:
        a = win32gui.GetActiveWindow()
        dataQ.put(a)
        time.sleep(1)

        # 終了措置
        if len(threading.enumerate()) == 2:
            print("are?")
            sys.exit()

#画像をとる
#アクティブ化して、alt+priおす、クリップボードからとってくる。
#
#
#
def captureScreen(maping,Mywindowname):
    timeNow= datetime.datetime.now()
    storetime = timeNow.strftime("%y%m%d%H%M%S")
    sc = pyautogui.screenshot(region=(maping))
    sc.save("./store/" + Mywindowname + str(storetime) + ".png")

# 終了措置
def stopingpower():
    sys.exit()

#一秒前のアクティブウィンドゲット
def getForeWindo():
    a = dataQ.get()
    return a

#GUI操作
def createWindowPop():
    root = tkinter.Tk()
    root.title("rara")
    root.geometry("100x150")
    # 10倍される？
    button = tkinter.Button(text="実行ボタン", height=10, width=15, command=getForeWindo)
    button.place(x=0, y=0)
    quit_botton = tkinter.Button(text="おわり！", height=10, width=15, command=stopingpower)
    quit_botton.place(x=0, y=180)
    root.attributes("-topmost", True)
    root.mainloop()


dataQ = queue.LifoQueue()

thread2 = threading.Thread(target=createWindowPop)
thread1 = threading.Thread(target=getForeWindow)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
