from tkinter import*
from tkinter import ttk

window = Tk()
window.title("Combobox example1")
window.geometry("300x250+100+100")

#combobx = ttk.Combobox(window, width=12,values=(10,20,30))
combobox = ttk.Combobox(window,width=12)
combobox['values'] = (10,20,30,40,50)
combobox.current(0)
combobox.pack()
window.mainloop()
