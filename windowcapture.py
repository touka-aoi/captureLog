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

global root
global dataQ

#LIFOかできた！！！

def getForeWindow():
    while True:
        a = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        dataQ.put(a)
        # print(len(threading.enumerate()))
        # ここ スマートじゃないポイント
        # print(threading.enumerate())
        # print(a)
        time.sleep(1)

        # 終了措置
        if len(threading.enumerate()) == 2:
            print("are?")
            sys.exit()

def stopingpower():
    sys.exit()

def getForeWindo():
    a = dataQ.get()
    b = win32gui.GetWindowRect(win32gui.FindWindow(None, a))
    print(b)
    # いけてまうかもしれん, #連打したらバグった あはははははは b[0] b[0] になってたぞ
    if (b[0] < 0 or b[1] < 0):
        #一回ずらす 灰天才
        pyautogui.moveTo(-500,-500)
        pyautogui.moveTo(b[0], b[1])
    else:
        pyautogui.moveTo(b[0],b[1])
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

# キューって何？

# root = tkinter.Tk()
dataQ = queue.LifoQueue()

thread2 = threading.Thread(target=createWindowPop)
thread1 = threading.Thread(target=getForeWindow)
thread1.start()
thread2.start()
thread1.join()
thread2.join()



#めがいたくなった ねる