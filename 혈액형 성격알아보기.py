from tkinter import*
from tkinter import messagebox
#함수
def result(혈액형):
    bt1["state"] = "disabled"
    bt2["state"] = "disabled"
    bt3["state"] = "disabled"
    bt4["state"] = "disabled"
    ##혈액형별 성격보여주기
    if 혈액형=="A":
        messagebox.showinfo("A형 성격", "A형은 소심한 성격의 소유자")
    elif 혈액형=="B":
        messagebox.showinfo("B형 성격","B형은 성격이 급하고 다혈질임")
    elif 혈액형=="O":
        messagebox.showinfo("O형 성격","O형은 성격이 급하고 다혈질임")
    elif 혈액형=="AB":
        messagebox.showinfo("AB형 성격","AB형은 성격이 급하고 다혈질임")
    w.after(1000,ready)
    def ready():
            text["text"] = "혈액형중 하나를 골라"
            bt1["state"] = "normal"
            bt2["state"] = "normal"
            bt3["state"] = "normal"
            bt4["state"] = "normal"

w = Tk()
w.title("혈액형별 성격")
w.geometry("600x400")
w.resizable(width = False,height = False) 

text = Label(w, text = "혈액형중 하나를 클릭하세여",font=("굴림",15,"bold"))
text.pack(pady = 10)   

p1 = PhotoImage(file = "A형.png")
p1 = p1.subsample(x=2)
bt1 = Button(w,image = p1,command = lambda:result("A"))
bt1.place(x = 70,y = 100)
p2 = PhotoImage(file = "B형.png")
p2 = p2.subsample(x=2)
bt2 = Button(w,image = p2,command = lambda:result("B"))
bt2.place(x = 200,y = 100)
p3 = PhotoImage(file = "O형.png")
p3 = p3.subsample(x=2)
bt3 = Button(w,image = p3,command = lambda:result("O"))
bt3.place(x = 330,y = 100)
p4 = PhotoImage(file = "AB형.png")
p4 = p4.subsample(x=2)
bt4 = Button(w,image = p4,command = lambda:result("AB"))
bt4.place(x = 460,y = 100)
w.mainloop()