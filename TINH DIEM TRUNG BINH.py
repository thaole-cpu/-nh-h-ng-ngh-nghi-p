n= int(input())
a=[float(i) for i in  input().split()]
t=max(a)
v= min(a)
m=[]
for i in a:
        if i !=t and i != v:
            m.append(i)
print("{:.2f}".format(sum(m) / len(m)))


