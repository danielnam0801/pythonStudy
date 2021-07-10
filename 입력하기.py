from tkinter import*

w=Tk()
w.title("거꾸로 말해요")
w.resizable(width = False,height = False)

def gukkuro():
    go=en.get()
    lb["text"] = go[::-1]
en = Entry(w,width = 10)
en.grid(row=0,column = 2)
en.focus_set()
lb = Label(w,text=" ")
lb.grid(row = 0,column = 1)
bt = Button(w,text = "입력하세요", command=gukkuro)
bt.grid(row = 0,column = 0)
w.mainloop()