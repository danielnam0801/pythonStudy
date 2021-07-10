from tkinter import *
def 계산():
    first=float(en1.get())
    second = float(en2.get())
    result = first*second
    lb5["text"] = "결과는" +str(result)+"입니다"

w = Tk()
w.title("곱셈 계산기")
w.geometry("500x50")

en1 = Entry(w,width=4)
en1.grid(row = 0,column=1)
en1.focus_set()

en2 = Entry(w,width = 4)
en2.grid(row = 1,column = 1)

lb1 = Label(w,text = "첫번쨰 수")
lb1.grid(row = 0,column =0)

lb2 = Label(w,text = "두번쨰 수")
lb2.grid(row = 1,column =0)

bt = Button(w, text = "계산",command = 계산)
bt.grid(row = 1,column = 3)

lb5 = Label(w, text = "곱셈 계산기입니다..")
lb5.grid(row = 0,column=3)

w.mainloop()