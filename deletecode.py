from tkinter import *
from tkinter import messagebox, ttk
employees = []
class Employees:
    def __init__(self, n, d, p, r):
        self.n = n
        self.d = d
        self.p = p
        self.r = r
def add():
    n = e1.get()
    d = e2.get()
    p = e3.get()
    r = e4.get()
    employees.append(Employees(n, d, p, r))
    tview.insert('', "end", text=n, values=(d, p, r))
    messagebox.showinfo("Add", "Successfully added")
def delete():
    selected_item = tview.selection()[0]
    tview.delete(selected_item)
def updatetreeview():
    # here where I am lost at I don't know what to do
    selected_item = tview.selection()[0]
master = Tk()
Label(master, text='Name').grid(row=0)
Label(master, text='Department').grid(row=1)
Label(master, text='Position').grid(row=2)
Label(master, text='Rate').grid(row=3)
tview = ttk.Treeview(master, columns=('Name', 'Position', 'Department','Rate'))
tview.grid(row=7, column=0, columnspan=10)
tview.heading('#0', text="Name")
tview.heading('#1', text="Department")
tview.heading('#2', text="Position")
tview.heading('#3', text="Rate")
e1 = Entry(master, width="30")
e2 = Entry(master, width="30")
e3 = Entry(master, width="30")
e4 = Entry(master, width="30")
e1.grid(row=0, column=1, pady=10)
e2.grid(row=1, column=1, pady=10)
e3.grid(row=2, column=1, pady=10)
e4.grid(row=3, column=1, pady=10)
b1 = Button(master, text="Add", width="25", command=add)
b1.grid(row=4, column=1, pady=10)
b2 = Button(master, text="Update", width="25")
b2.grid(row=5, column=1, pady=10)
b2 = Button(master, text="Delete", width="25", command=delete)
b2.grid(row=6, column=1, pady=10)
mainloop()