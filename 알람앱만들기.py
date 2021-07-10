from tkinter import*
from tkinter import messagebox
import time
hour,minu = -1,-1

def 알람설정():
    global hour,minu
    hour = int(en1.get())
    minu = int(en2.get())
    lb2["text"] = "알람이 %d시 %d분으로 설정되었습니다" %(hour,minu)

def 시간출력(): 
    t = time.localtime()
    lb1["text"] = "%d:%d:%d"%(t.tm_hour,t.tm_min,t.tm_sec)
    if t.tm_hour == hour and t.tm_min == minu and t.tm_sec==0:
        messagebox.showinfo("알람","알람시가닝 되었습니다. 알람을 끄려면 확인해주세요!")
    w.after(1000,시간출력)

w = Tk()
w.title("알람 시계")
w.geometry("500x300")
w.resizable(width = False,height = False)
     
lb1 = Label(w,width = 20, font = ("굴림",30,"bold"))
lb1.place(x=10,y=10)
lb2 = Label(w, text = "알람 시간을 설정하세요.",font = ("바탕체",15),fg = "blue")
lb2.place(x=170,y=80)

en1 = Entry(w)
en1.place(x=200,y=120)
lb3 = Label(w,text = "시")
lb3.place(x=350,y=120)
en2 = Entry(w)
en2.place(x=200,y=150)
lb4 = Label(w,text = "분")
lb4.place(x=350,y=150)

bt = Button(w, text = "설정",command = 알람설정)
bt.place(x = 400,y = 30)
시간출력()
w.mainloop()