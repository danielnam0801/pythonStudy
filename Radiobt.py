from tkinter import *
window = Tk()
window.title("Radiobutton example")
window.geometry("400x300")

Label(window,text="동물을 선택하세요").pack()

animal_var = IntVar()
btn_hipo=Radiobutton(window,text="하마",value=1,variable=animal_var)
btn_hipo.select()
btn_cat=Radiobutton(window,text="고양이",value=2,variable=animal_var)
btn_tiger=Radiobutton(window,text="호랑이",value=3,variable=animal_var)

btn_hipo.pack()

btn_cat.pack()

btn_tiger.pack()

Label(window, text = "동물을선택하세요").pack()
animal2_var = StringVar()
btn_hipo2 = Radiobutton(window, text="하마",value="하마",variable=animal2_var)
btn_hipo2.select()
btn_cat2=Radiobutton(window,text="고양이",value="고양이",variable=animal2_var)
btn_tiger2=Radiobutton(window,text="호랑이",value="호랑이",variable=animal2_var)

btn_hipo2.pack()

btn_cat2.pack()

btn_tiger2.pack()

def btncmd():
    print(animal_var.get())
    print(animal2_var.get())
    msg="선택결과:%d,%s"%(animal_var.get(),animal2_var.get())
    lb_result['text'] = msg

btn = Button(window,text = "선택", command=btncmd)
btn.pack()
lb_result = Label(window,text="선택 결과:")
lb_result.pack()

window.mainloop()