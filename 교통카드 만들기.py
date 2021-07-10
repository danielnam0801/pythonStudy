from tkinter import*
from tkinter import messagebox

num = 10000
bus = 1500
sub = 1200

w = Tk()

lb1 = Label(w, font = ("굴림",10))
lb1.grid(row=0,column=0)    
lb1["text"] = "잔액은 %d원 남았습니다" % (num)

def popup():
    global num
    num -= bus
    lb1["text"] = "잔액은 %d원 남았습니다" % (num)
    messagebox.showinfo("버스","1500원이 차감되었습니다")

bt = Button(w,text = '버스', command = popup)
bt.grid(row=1,column=0)

def popup1():
    global num
    num -= sub
    lb1["text"] = "잔액은 %d원 남았습니다" % (num)
    messagebox.showinfo("지하철","1200원이 차감되었습니다")

bt2 = Button(w,text = '지하철',command = popup1)
bt2.grid(row=1,column= 3)

def popup2():
    global num
    add = int(en1.get())
    num += add
    lb1["text"] = "잔액은 %d원 남았습니다" % (num)
bt3 = Button(w,text = ("충전하고싶은 금액을 입력하세요"),command = popup2)
bt3.grid(row=3,column=2)

en1 = Entry(w, width=6)
en1.grid(row=3,column=3)

w.mainloop()

