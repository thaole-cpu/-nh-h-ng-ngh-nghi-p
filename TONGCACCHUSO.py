import math
def check(n):
    a=[]
    s=0
    for i in n:
        if i.isalpha():
            a.append(i)
        elif i.isdigit():
             s += int(i)
    a.sort()
    #chuyen ki tu thanh chuoi
    st = ''.join(a)
    m = str(st)+str(s)
    return m
for v in range(int(input())) :
    n=input()
    print(check(n))