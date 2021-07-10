from tkinter import*

w = Tk()

w.title("bmi계산기")
w.geometry("200x120")
w.resizable(width = False,height=False)

def 계산():
    hei = int(en1.get())/100
    wei = int(en2.get())
    bmi = wei/(hei*hei)
    if(bmi<18.5):
        lb3["text"] = "당신의 bmi지수는 %d "%(bmi)
        lb3["bg"] = 'red'  
    if(18.5< bmi <23):
        lb3["text"] = "당신의 bmi지수는 %d "%(bmi)
        lb3["bg"] = 'orange'  
    if(23<bmi<25):
        lb3["text"] = "당신의 bmi지수는 %d "%(bmi)
        lb3["bg"] = 'yellow'  
    if(bmi>25):
        lb3["text"] = "당신의 bmi지수는 %d "%(bmi)
        lb3["bg"] = 'blue'  

en1 = Entry(w,width=10)
en1.grid(row =0 ,column = 1)
en1.focus_set()
en2 = Entry(w,width=10)
en2.grid(row =1 ,column = 1)
en2.focus_set()

lb = Label(w,text = "키(cm)")
lb.grid(row = 0,column = 0)
lb2 = Label(w,text = "몸무게")
lb2.grid(row = 1,column = 0)
lb2.grid()
lb3 = Label(w,text = "당신의bmi지수는")
lb3.grid(row = 3,column = 0)
lb3.grid()

bt = Button(w,text = "결과확인",command = 계산)
bt.grid(row = 2,column = 0)


w.mainloop()