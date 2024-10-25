a=[]
while len(a) <10:
   a = [int(i) for i in input().split()]
for i in range (len(a)):
       a[i] %= 42
print(len(set(a)))