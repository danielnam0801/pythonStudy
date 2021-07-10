from tkinter import*
from tkinter import ttk

window = Tk()
window.title("Combobox example2")
window.geometry("300x250+100+100")

sVar = StringVar()
values = [str(i)+"월" for i in range(1,13)]
#combobox = ttk.Combobox(window, width = 12, caluese=(10,20,30))
combobox = ttk.Combobox(window, width= 12, textvariable =sVar)
combobox['values'] = values
combobox.current(0)
combobox.grid(row=0,column=0)

def btn1_run():
    selection = "선택된값은" + str(sVar.get())
    label['text'] = selection
btn1 = Button(window, text="값출력",command = btn1_run)
btn1.grid(row=0, column=1)
sVar2 = StringVar()
values = [str(i)+"일" for i in range(1,32)]
readonly_combobox = ttk.Combobox(window, width = 12, height = 10)
readonly_combobox['textvariable'] = sVar2
readonly_combobox['values'] = values
readonly_combobox.current(0)
readonly_combobox.grid(row=1, column=0)

def btn2_run():
    selection = str(sVar2.get())
    label2['text'] = selection
btn2 = Button(window, text = "값 출력", command=btn2_run)
btn2.grid(row=1, column=1)

label = Label(window)
label.grid(row=2, column = 0)
label2 = Label(window)
label2.grid(row=2, column=1)

window.mainloop()