from tkinter import*
from tkinter import messagebox

window=Tk()

def info_box():
    messagebox.showinfo("정보", "Do nothing.")

def quit():
    window.destroy()
    window.quit()

def help_box():
    messagebox.showinfo("정보", "Ver.01")

menu_main = Menu(window)
filemenu = Menu(menu_main, tearoff=0)
filemenu.add_command(label="새 파일", command=info_box)
filemenu.add_command(label="열기", command=info_box)
filemenu.add_command(label="저장", command=info_box)
filemenu.add_separator()
filemenu.add_command(label="종료", command=quit)
menu_main.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menu_main, tearoff=0)
helpmenu.add_command(label="About", command=help_box)
menu_main.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menu_main)

window.mainloop()