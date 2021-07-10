from tkinter import*

window = Tk()
window.title("Listbox example1")
window.geometry("250x200")
window.resizable(False,False)

listbox = Listbox(window)
listbox.insert(1,"Python")
listbox.insert(2,"C")
listbox.insert(3,"C++")
listbox.insert(4,"Java")
listbox.insert(5,"JavaScript")
listbox.insert(6,"PHP")
listbox.insert(7,"C#")
listbox.pack()

window.mainloop()
 