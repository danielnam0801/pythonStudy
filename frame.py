from tkinter import*

window = Tk()
window.title("Frame example")
window.geometry("250x250")

frame = Frame(window)
frame.pack()

btn1 = Button(frame,text = "Red",fg = "red")
btn1.pack(side = LEFT)
btn2 = Button(frame,text = "Green",fg = "green")
btn2.pack(side=LEFT)

btn3 = Button(frame,text = "Blue",fg = "blue")
btn3.pack(side=LEFT)
window.mainloop()