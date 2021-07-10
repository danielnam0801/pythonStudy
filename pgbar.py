from tkinter import*
from tkinter import ttk
from time import sleep

window = Tk()
window.title("Progressbar example1")
window.geometry("300x250+100+100")

pg_bar = ttk.Progressbar(window, maximum=100, length = 286, mode = "indeterminate")
pg_bar.start(10)
pg_bar.pack()

def btncmd():
    pg_bar.stop()

btn = Button(window, text="중지", command=btncmd)
btn.pack()

window.mainloop()