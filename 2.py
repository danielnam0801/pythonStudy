from tkinter import*
from tkinter import messagebox

window = Tk()
window.title("Listbox example")
window.geometry("640x480+100+100")
window.resizable(False,False)

def addAction():
    msg = str(listbox.size())+"번"
    listbox.insert(END,msg)

def delAction():
    if listbox.size()>0:
        listbox.delete(END)
    else:
        messagebox.showinfo("알림","목록이 존재하지않습니다.")

listbox = Listbox(window,selectmode = 'extended',height=5)
listbox.pack()

addbtn = Button(window,text="Add",command = addAction)
addbtn.pack()
delbtn = Button(window,text="Delete",command = delAction)
delbtn.pack()

window.mainloop()