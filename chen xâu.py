def chen(s1,s2,p):
    p -=1
    if len(s1) < p:
        p=len(s1)
    kq=s1[:p]  + s2 + s1[p:]
    return kq
s1=input()
s2=input()
p=int(input())
print(chen(s1,s2,p))