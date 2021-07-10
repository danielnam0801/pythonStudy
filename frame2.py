from tkinter import*

window = Tk()
window.title("Frame example2")
window.resizable(False,False)

def click(key):
    if key == 'C':
        en.delete(0,END)
    elif key == '=':
        go = en.get()
        en.delete(0,END)
        result = eval(go)
        en.insert(END,str(result))
        print (result)
    else:
        go = en.get()
        go = go + key
        print(go)
        en.insert(END,key)

top_panel = Frame(window)
top_panel.grid(row=0,column=0,columnspan=2,sticky=N)
en = Entry(top_panel,width = 45,bg = "skyblue")
en.grid()

num_panel = Frame(window)
num_panel.grid(row=1,column=0,sticky = W)
number_list = ['7','8','9','4','5','6','1','2','3','0','.','=']
r=0
c=0

for btext in number_list:
    btn = Button(num_panel,text = btext,width = 5,command=lambda a =btext: click(a))
    btn.grid(row=r,column=c)
    c=c+1
    if c>2:
        c=0
        r=r+1
oper_panel = Frame(window)
oper_panel.grid(row=1,column=1,sticky=E)
oper_list = ['*','/','+','-','(',')','C']
r=0
c=0
for btext in oper_list:
    btn = Button(oper_panel,text = btext,width = 5,command=lambda a =btext:click(a))
    btn.grid(row=r,column=c)
    c=c+1
    if c>1:
        c=0
        r=r+1

window.mainloop()