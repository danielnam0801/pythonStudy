from tkinter import *

w = Tk()
w.resizable(width = False, height = False)
photo = PhotoImage(file = "cat.png")

lb1 = Label(w,image = photo)
lb1.pack(side = "left")

lb2 = Label(w, text = "고양이 사진")
lb2.pack(side = "right")
w.mainloop()