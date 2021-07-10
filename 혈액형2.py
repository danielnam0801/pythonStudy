from tkinter import*
from tkinter import messagebox
import random as r

num,num2 =0,0
com,h=0,0
def result( a ):    
    global com,h
    b = r.randint(1,3)
    if a == "가위":
        img1 = PhotoImage(file = "가위.png")
        img1 = img1.subsample(x=1)
        lp1.config(image=img1)
        lp1.image = img1
        a = 1
        if b - a == 1:
            com=com+1     
        if b - a == 2:
            h = h+1 

    elif a == "바위":
        img2 = PhotoImage(file = "바위.png")
        img2 = img2.subsample(x=1)
        lp1.config(image=img2)
        lp1.image = img2
        a = 2
        
        if b - a == 1:
            com=com+1     
        if a - b == 1:
            h = h+1
        
    else:
        img3 = PhotoImage(file = "보.png")
        img3 = img3.subsample(x=1)
        lp1.config(image=img3)
        lp1.image = img3
        a = 3
        if a - b == 2:
            com=com+1     
        if a - b == 1:
            h = h+1
    if b==1:
        img1 = PhotoImage(file = "가위.png")
        img1 = img1.subsample(x=1)
        lp2.config(image=img1)
        lp2.image = img1
       
    if b==2:
        img2 = PhotoImage(file = "바위.png")
        img2 = img2.subsample(x=1)
        lp2.config(image=img2)
        lp2.image = img2
    if b==3:
        img3 = PhotoImage(file = "보.png")
        img3 = img3.subsample(x=1)
        lp2.config(image=img3)
        lp2.image = img3
        
    점수설정()
    점수설정2()

    bt1["state"] = "disabled"
    bt2["state"] = "disabled"
    bt3["state"] = "disabled"


    w.after(1000,ready)

w = Tk()
w.title("혈액형별 성격")
w.geometry("600x400")
w.resizable(width = False,height = False)

text = Label(w, text = "가위바위보중 하나를 클릭하세요",font = ("굴림",15,"bold"))
text.pack(pady = 10)


def 점수설정():
    global num
    num = int(h)     
    lb1_1["text"] = "%d" %num 

def 점수설정2():
    global num2
    num2 = int(com)
    lb2_2["text"] = "%d" %num2

lb1 = Label(w, text = "사람", font = ("바탕체",15),fg = "blue")
lb1.place(x= 100,y=50)
lb1_1 = Label(w, text = "0", font = ("바탕체",15),fg = "black")
lb1_1.place(x= 200,y=50)


lb2 = Label(w, text = "컴퓨터", font = ("바탕체",15),fg = "red")
lb2.place(x= 440,y=50)
lb2_2 = Label(w, text = "0", font = ("바탕체",15),fg = "black")
lb2_2.place(x= 360,y=50)

pp1 = PhotoImage(file = "물음표.png")
pp1 = pp1.subsample(x=1)
lp1 = Label(w,image = pp1)
lp1.place(x = 100,y=100)

pp2 = PhotoImage(file = "물음표.png")
pp2 = pp2.subsample(x=1)
lp2 = Label(w,image = pp2)
lp2.place(x = 300,y=100)

p1 = PhotoImage(file = "가위.png")
p1 = p1.subsample(x=2)
bt1 = Button(w,image = p1, command = lambda : result("가위"))
bt1.place(x = 100,y = 290)

p2 = PhotoImage(file = "바위.png")
p2 = p2.subsample(x=2)
bt2 = Button(w,image = p2,command = lambda:result("바위"))
bt2.place(x = 250,y = 290)

p3 = PhotoImage(file = "보.png")
p3 = p3.subsample(x=2)
bt3 = Button(w,image = p3,command = lambda:result("보"))
bt3.place(x = 400,y = 290)


def ready():
    lp1.config(image=pp1)
    lp1.image = pp1
    lp2.config(image=pp2)
    lp2.image = pp2
    
    bt1["state"] = "normal"
    bt2["state"] = "normal"
    bt3["state"] = "normal"



w.mainloop()   