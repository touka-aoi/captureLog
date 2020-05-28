#参考 https://ocome85.work/2019/11/04/37/
#アクティブウィンドウ名
#アクティブウィンドいち
#アクティブウィンドウサイズ
#キャプチャーでおk

import tkinter
import pyautogui
import win32gui
import win32con
import threading
import time
import sys

global root

def getForeWindow():
    while True:
        a = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        print(len(threading.enumerate()))
        print(threading.enumerate())
        time.sleep(1)
        if len(threading.enumerate()) == 2:
            print("are?")
            sys.exit()

def stopingpower():
    sys.exit()

def getForeWindo():
    a = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    print(a)

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



thread1 = threading.Thread(target=getForeWindow)
thread2 = threading.Thread(target=createWindowPop)
thread1.start()
thread2.start()
thread1.join()
thread2.join()



#めがいたくなった ねる