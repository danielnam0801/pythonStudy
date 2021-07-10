from tkinter import*
from tkinter import messagebox

def click(event):
    messagebox.showinfo("안녕","화이팅!")

w = Tk()

lb = Label(w, text = "마우스 왼쪽을 눌러보세요")
lb.pack()
lb.bind("<Button-1>",click)

w.mainloop()
