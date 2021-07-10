from tkinter import*
from tkinter import messagebox  
from tkinter import filedialog

window=Tk()


def Load():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("Text files", "*.txt"),("python piles", "*.py"), ("all files", "*.*")))
    print(filename)
        
    data=open(filename,'rt',encoding="utf-8")
        
    text.delete('1.0', END)
        
    text.insert(END,data.read())

    filename.close()

def Save():
    filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                          filetypes=(("Text files", "*.txt"),("python piles", "*.py"),("all files", "*.*")))
    print(filename)

    f=open(filename,'wt', encoding="utf-8")

    if f is None:
        return

    ts = str(text.get(1.0, END))
    f.write(ts)
    f.close()




def new_box():
    text.delete('1.0',END)
def open_box():
    Load()

def save_box():
    Save()


frame = Frame(window)
frame.pack()


scrollbar = Scrollbar(frame)
scrollbar.pack(side = "right", fill= 'y')

text = Text(frame,height=50,yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)

def quit():
    window.destroy()
    window.quit()

def help_box():
    messagebox.showinfo("정보", "Ver.01")

menu_main = Menu(window)
filemenu = Menu(menu_main, tearoff=0)
filemenu.add_command(label="새 파일", command=new_box)
filemenu.add_command(label="열기", command=open_box)
filemenu.add_command(label="저장", command=save_box)
filemenu.add_separator()
filemenu.add_command(label="종료", command=quit)
menu_main.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menu_main, tearoff=0)
helpmenu.add_command(label="About", command=help_box)
menu_main.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menu_main)

window.mainloop()