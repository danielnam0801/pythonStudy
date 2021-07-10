from tkinter import*
from tkinter import messagebox

w = Tk()
w.title("가위바위보")
w.geometry("600x400")
w.resizable(width = False,height = False)

def junsung():
    #print("가위 바위 보 중 하나를 클릭하세요.")
    pass
def 점수설정():
    global num
    num = int()
    
    lb2["text"] = "사람     %d" %num 
def 점수설정2():
    global num2
    num2 = int()
    
    lb2["text"] = "%d     컴퓨터"&num2

lb1 = Label(w, text="가위 바위 보 중 하나를 클릭하세요.")
lb1.pack()


btn1 = Button(w, text="Run", command=junsung)
btn1.pack()

w.mainloop()    