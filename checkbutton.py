from tkinter import*

window=Tk()
window.title("CheckButton example")
window.geometry("500x500")

canvas = Canvas(window,width = 400,height = 400)
photo = PhotoImage(file = "하마.png")
cImg = PhotoImage()

image = canvas.create_image(15,15,image = photo, disabledimage=cImg,anchor=NW)
canvas.pack()

chkvar = IntVar()
chkbox = Checkbutton(window,text="이미지 보지 않기",variable=chkvar)
chkbox.pack()

def btncmd():
    print(chkvar.get())
    if chkvar.get():
        canvas["state"] = DISABLED
    else:
        canvas["state"] = NORMAL

btn=Button(window,text="클릭",command=btncmd)
btn.pack()

window.mainloop()