from tkinter import*
from tkinter import messagebox

window = Tk()
window.title("회원관리")
window.geometry("200x150+100+100")

def join_box():
    window2 = Tk()
    window2.title("회원가입")
    window2.geometry("230x100+100+100")
    
    def gaib():
        if entry2.get() == entry3.get():
            
            id = entry.get()
            f = open('id.txt','w')
            f.write(id)
            f.close()
            ps = entry2.get()
            f = open('ps.txt','w')
            f.write(ps)
            f.close()

        else:
            messagebox.showinfo("확인","비밀번호가다릅니다") 


    def cancel():
        window2.quit()
        window2.destroy()

    lb = Label(window2, text = "사용할아이디")
    lb.grid(row = 0, column = 0)
    lb2 = Label(window2, text = "사용할패스워드")
    lb2.grid(row = 1, column = 0)
    lb3 = Label(window2, text = "패스워드 재입력")
    lb3.grid(row = 2, column = 0)
    
    entry=  Entry(window2)
    entry.grid(row=0,column=1)
    entry2=  Entry(window2)
    entry2.grid(row=1,column=1)
    entry3=  Entry(window2)
    entry3.grid(row=2,column=1)
    
    btt = Button(window2,text = "가입하기",command = gaib)
    btt.grid(row=3,column=0)
    btt2 = Button(window2,text = "취소",command = cancel)
    btt2.grid(row=3,column=1)

    window2.mainloop()

def login_box():
    window3 = Tk()
    window3.title("로그인")
    window3.geometry("200x150+100+100")

    def log():
        f = open('id.txt','r')
        id = f.read()    
        f.close()
        f = open('ps.txt','r')
        ps = f.read()
        f.close()
       
        if entry11.get() == id and entry22.get()== ps:
             messagebox.showinfo("로그인성공", "%s님안녕하세요"%id) 
        else:
            messagebox.showerror("로그인실패","비밀번호가 다릅니다")
        
    def can():
        window3.quit()
        window3.destroy()


    lb4 = Label(window3, text = "아이디")
    lb4.grid(row = 0, column = 0)
    lb5 = Label(window3, text = "패스워드")
    lb5.grid(row = 1, column = 0)
    entry11=  Entry(window3)
    entry11.grid(row=0,column=1)
    entry22=  Entry(window3)
    entry22.grid(row=1,column=1)
      
    bttt = Button(window3,text = "로그인",command = log)
    bttt.grid(row=3,column=0)
    bttt2 = Button(window3,text = "취소",command = can)
    bttt2.grid(row=3,column=1)
    
    window3.mainloop()
    

bt = Button(text = "회원가입",command = join_box)
bt.grid(row=0,column=0)
bt2 = Button(text = "로그인",command = login_box)
bt2.grid(row=0,column=1)

window.mainloop()
