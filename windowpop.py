import tkinter
from tkinter import messagebox

def button_click():
    # タイトル 中身 かな？
    #関数つかうのきもい どうにかならないのん？
    input_value = input_box.get()
    messagebox.showinfo("クリックイベント", f"実行ボタンがクリックされました きさま！！{input_value}ってかいたな！！")



root = tkinter.Tk()
root.title("Touka no saisyono GUI")
root.geometry("360x240")
# イベントループ イベントディスパッチャ？ assyncとかのやつかな？ まああいいや うーん コルーチンとかの勉強ほんとにしないとなぁ
input_box = tkinter.Entry(width=40)
# 起点の場所
input_box.place(x=10, y=100)
#Entryのgetファンクションで入力をとれる
input_label = tkinter.Label(text="ラベル")
input_label.place(x=10, y=70)

#command で 関数実行できる
button = tkinter.Button(text="実行ボタン", command=button_click)
button.place(x=10, y=130)

#常に全面表示
root.attributes("-topmost", True)

root.mainloop()



#これでコメントとってどーん組み合わせる？
#まあGUIなのはしゃーなし！！！！