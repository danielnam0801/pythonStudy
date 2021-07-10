from tkinter import*
from tkinter import messagebox

w = Tk()
w.title("팝업창")
w.resizable(width = False, height = False)

def popup():
    messagebox.showinfo("팝업창","확인을 누르세요")

bt = Button(w,text = "누르면 팝업창이 뜹니다.",command = popup)
bt.place(x = 10,y = 10)

w.mainloop()