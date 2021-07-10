from tkinter import*
from tkinter import ttk
from time import sleep

window = Tk()
window.title("Progressbar example1")
window.geometry("300x250+100+100")

def run_pgbar():
    pg_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        p_var2.set(i)
        pg_bar.update()
        lb_val["text"] = p_var2.get()

p_var2 = DoubleVar()
pg_bar = ttk.Progressbar(window, maximum = 100, length = 286, variable = p_var2)
pg_bar.grid(row=0, column=0, padx=20, pady=20)

lb_val = Label(window, text="0", width=5)
lb_val.grid(row=0, column=1, padx=5)
btn1 = Button(window, text = "Run Progressbar", command=run_pgbar)
btn1.grid(row=1, column=0)
window.mainloop()