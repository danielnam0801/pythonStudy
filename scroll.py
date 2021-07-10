from tkinter import*
from tkinter import messagebox

window = Tk()
window.title("Listbox example")
#window.resizable(False, False)

def addAction():
    msg = str(listbox.size()) + "번"
    listbox.insert(END, msg)

def delAction():
    if listbox.size()>0:
        listbox.delete(END)
    else:
        messagebox.showinfo("알림","No list")

frame = Frame(window)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill='y')

listbox = Listbox(frame,selectmode='extended', height= 10, yscrollcommand=scrollbar.set)
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)

addbtn = Button(window, text="Add", command=addAction)
addbtn.pack()
delbtn = Button(window,text="Delete", command=delAction)
delbtn.pack()
    
window.mainloop()