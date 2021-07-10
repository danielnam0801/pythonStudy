from tkinter import*

w=Tk()
w.resizable(width = False, height = False)

bt = Button(w,text = "파이썬 끄기", command = quit)

bt.grid(row =0,column = 0)

w.mainloop()