from tkinter import*
from tkinter import messagebox

window = Tk()
window.title("Listbox example")
#window.resizable(False, False)

def addAction():
    msg = entry.get() 
    print(msg)
    listbox.insert(END, msg)

def delAction():
    if listbox.size()>0:
        listbox.delete(END)
    else:
        messagebox.showinfo("알림","No list")

#첫번쨰 칸
frame = Frame(window)
frame.grid(row=0, column=0)

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill='y')

listbox = Listbox(frame,selectmode='extended', height= 10, yscrollcommand=scrollbar.set)
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)

#엔트리포함한 프레임1
frame11 = Frame(window)
frame11.grid(row=1, column=0)

entry=  Entry(frame11)
entry.grid(row=0,column=0, columnspan=2)

addbtn = Button(frame11, text="Add", command=addAction)
addbtn.grid(row=1, column=0)
delbtn = Button(frame11,text="Delete", command=delAction)
delbtn.grid(row=1, column=1)
    
def add1Action():
    msg1 = entry2.get()
    listbox1.insert(END, msg1)

def del1Action():
    if listbox1.size()>0:
        listbox1.delete(END)
    else:
        messagebox.showinfo("알림","No list")

#두번쨰 칸
frame2 = Frame(window)
frame2.grid(row=0,column=2)

scrollbar1 = Scrollbar(frame2)
scrollbar1.pack(side="right", fill='y')

listbox1 = Listbox(frame2,selectmode='extended', height= 10, yscrollcommand=scrollbar1.set)
listbox1.pack(side="left")
scrollbar1.config(command=listbox1.yview)

#엔트리포함한 프레임2
frame22 = Frame(window)
frame22.grid(row=1, column=2)

entry2 = Entry(frame22)
entry2.grid(row=0,column=0,columnspan=2) 

addbtn1 = Button(frame22, text="Add", command=add1Action)
addbtn1.grid(row=1, column=0)
delbtn1 = Button(frame22,text="Delete", command=del1Action)
delbtn1.grid(row=1, column=1)


def rightAction():
    pos = listbox.curselection()
    rm = listbox.get(pos)
    listbox.delete(pos)
    listbox1.insert(END, rm)
    

def leftAction():
    pos2 = listbox1.curselection()
    rm2 = listbox1.get(pos2)
    listbox1.delete(pos2)
    listbox.insert(END, rm2)
    
frame3 = Frame(window)
frame3.grid(row=0,column=1)

rightbtn = Button(frame3, text='->', command=rightAction)
rightbtn.grid(row=1,column=1)
leftbtn = Button(frame3, text='<-', command=leftAction)
leftbtn.grid(row=2,column=1)
    
window.mainloop()