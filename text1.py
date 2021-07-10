'''
print("아이디를 입력하세요: ")
id = input()
print("패스워드를 입력하세요: ")
pw = input()

f = open('id.txt','w')
f.write(id)
f.close()

f = open('pw.txt','w')
f.write(pw)
f.close()
'''

f = open('id.txt','r')
s = f.read()
print(s)
f.close()

f = open('pw.txt','r')
s = f.read()
print(s)
f.close()