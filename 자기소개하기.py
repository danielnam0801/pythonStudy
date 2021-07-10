from tkinter import*
introduce = """이름:김코딩
나이:13세
사는곳:목동12단지 1300동 3901호
학교:소엔코딩학원
소속:6학년9반
별명:코딩천재
학교성적:비밀
좋아하는 사람:어무니
인삿말:똑똑한 사람이 되는게 저의 꿈입니다"""

w=Tk()
w.title("김코딩의 자기소개")
w.resizable(width = False,height = False)
photo = PhotoImage(file = "사진.png")
photo = photo.subsample(x=3)
lb1 = Label(w, image = photo)
lb1.pack(side = "left")
lb2 = Label(w,text = introduce,justify = "left")
lb2.pack(side = "right")
w.mainloop()