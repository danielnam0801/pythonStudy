from tkinter import*
from tkinter import messagebox
import random as r
#리스트-주사위 이미지 보관
dice = []
#함수-주사위던지기
def 주사위():
    a=r.randint(1,6)
    b = r.randint(1,6)
    lb1["image"] = dice[a-1]
    lb2["image"] = dice[b-1]
    msg["text"] = str(a+b)+ "칸 이동하세요~"
#윈도우 창설정
w = Tk()
w.title("부루마블 주사위")
w.geometry("260x120")
w.resizable(width = False,height = False)
#버튼
bt = Button(w, text = "주사위\n던지기", command = 주사위)
bt.place(x=150,y=30)
dice1 = PhotoImage(file = "1.png")
dice2 = PhotoImage(file = "2.png")
dice3 = PhotoImage(file = "3.png")
dice4 = PhotoImage(file = "4.png")
dice5 = PhotoImage(file = "5.png")
dice6 = PhotoImage(file = "6.png")
dice.append(dice1.subsample(x=3))
dice.append(dice2.subsample(x=3))
dice.append(dice3.subsample(x=3))
dice.append(dice4.subsample(x=3))
dice.append(dice5.subsample(x=3))
dice.append(dice6.subsample(x=3))
lb1 = Label(w,image = dice[0])
lb1.place(x=10,y=30)
lb2 = Label(w,image = dice[0])
lb2.place(x=80,y=30)

msg = Label(w,text = "버튼을 누르면 주사위를 던집니다")
msg.place(x=0,y=10)
w.mainloop()