from tkinter import *
def 계산():
    first=float(en1.get())
    second = float(en2.get())
    result = first/second
    lb7["text"] = "이교통 수단의 평균 속력은 " +str(result)+"km/h입니다"

w = Tk()
w.title("속력 계산기")
w.geometry("500x50")

en1 = Entry(w,width=4)
en1.grid(row = 0,column=1)
en1.focus_set()

# 이동거리 입력
en2 = Entry(w,width = 4)
en2.grid(row = 1,column = 1)

#레이블
lb1 = Label(w,text = "이동거리",)
lb1.grid(row = 0,column =0)

#레이블
lb2 = Label(w,text = "이동시간")
lb2.grid(row = 1,column =0)

#버튼
bt = Button(w, text = "계산",command = 계산)
bt.grid(row = 1,column = 4)

#레이블
lb5 = Label(w, text = "km")
lb5.grid(row = 0,column=3)


lb6 = Label(w, text = "h")
lb6.grid(row = 1,column=3)

lb7 = Label(w, text = "이동거리와 이동시간을 입력해라")
lb7.grid(row = 1,column = 5 )

w.mainloop()