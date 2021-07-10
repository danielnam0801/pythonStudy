import tkinter as tk
import tkinter.ttk as ttk

ws = tk.Tk()
ws.title("PythonGuides")
ws['bg'] = "#fb0"

tv = ttk.Treeview(ws, columns = (1,2,3), show = 'headings', height=8)
tv.pack()

tv.heading(1,text="name")
tv.heading(2,text="eid")
tv.heading(3,text="Salary")

def update_item():
    selected = tv.focus()
    temp = tv.item(selected, 'values')
    sal_up = round( float(temp[2])+ float(temp[2])*0.5,2)
    tv.item(selected,values=(temp[0],temp[1], sal_up))

data = [('Vineet','e11',1000.0), ('Anil', 'e12',1100.0),('Vinod', 'e13',1200.0),('Vimal', 'e14',1300.0),('Manjeet', 'e15',1400.0)]
for i in range(5):
    tv.insert(parent='',index=i,iid=i,text='',values=data[i])

tk.Button(ws,text="Increment Salary",command=update_item).pack()

style=ttk.Style()
style.theme_use("default")
style.map("Treeview")

ws.mainloop()