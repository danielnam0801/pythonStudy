def hap(a,b):
    c = a+b
    return c
print(hap(3,5))

zz = (lambda a,b :a+b)
print(zz(3,5))

qq = (lambda:hap(3,5))
print(qq())