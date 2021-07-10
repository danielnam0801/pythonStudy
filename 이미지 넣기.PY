from tkinter import *
w = Tk()
photo = PhotoImage(file="cat.png")
lb = Label(w,image=photo)
lb.pack()
w.mainloop()