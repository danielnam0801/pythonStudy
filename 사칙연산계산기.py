from tkinter import*

w = Tk()
w.title("bmi계산기")
w.geometry("150x150")
w.resizable(width = False,height=False)

def func(a):
    go = en.get()
    go = go + a
    print(go)
    en.insert(END,a)

def delete():
    en.delete(0, END)

def sum():
    go = en.get()
    en.delete(0,END)
    result = eval(go)
    en.insert(END,str(result))
    print(result)

en = Entry(w,width = 20)
en.grid(row =0 ,column = 0, columnspan = 4)
en.focus_set()

btn_delete = Button(w,text="C",command = delete).grid(row = 4,column=0,ipadx=10)
bt = Button(w,text = "0",command = lambda:func('0')).grid(row=4,column=1,ipadx=10)
btn_sum = Button(w,text="=",command = sum).grid(row = 4,column=2,ipadx=10)
btn_na = Button(w,text="/",command = lambda:func('/')).grid(row = 4,column=3,ipadx=10)

bt1 = Button(w,text = "1",command = lambda:func('1')).grid(row=3,column=0,ipadx=10)
bt2 = Button(w,text = "2",command = lambda:func('2')).grid(row=3,column=1,ipadx=10)
bt3 = Button(w,text = "3",command = lambda:func('3')).grid(row=3,column=2,ipadx=10)
btn_ad = Button(w,text="x",command = lambda:func('*')).grid(row = 3,column=3,ipadx=10)

bt4 = Button(w,text = "4",command = lambda:func('4')).grid(row=2,column=0,ipadx=10)
bt5 = Button(w,text = "5",command = lambda:func('5')).grid(row=2,column=1,ipadx=10)
bt6 = Button(w,text = "6",command = lambda:func('6')).grid(row=2,column=2,ipadx=10)
btn_minus = Button(w,text="-",command = lambda:func('-')).grid(row = 2,column=3,ipadx=10)
bt7 = Button(w,text = "7",command = lambda:func('7')).grid(row=1,column=0,ipadx=10)
bt8 = Button(w,text = "8",command = lambda:func('8')).grid(row=1,column=1,ipadx=10)
bt9 = Button(w,text = "9",command = lambda:func('9')).grid(row=1,column=2,ipadx=10)
def plus_b():
    func('+')
btn_plus = Button(w,text="+",command = plus_b).grid(row = 1,column=3,ipadx=10)

w.mainloop()