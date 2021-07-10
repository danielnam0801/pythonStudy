from tkinter import *
import time

def 시간출력():
    t = time.localtime()
    lb1["text"]= "%d:%d:%d" %(t.tm_hour,t.tm_min,t.tm_sec)
    w.after(1000,시간출력)

w=Tk()
w.title("시계")
w.resizable(width = False,height = False)

lb1 = Label(w, width = 20 , font= ("굴림",30,"bold"))
lb1.pack()
시간출력()
w.mainloop()